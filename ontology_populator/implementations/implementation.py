from typing import List, Union

from rdflib.collection import Collection

from common import *

LiteralValue = Union[str, bool, int, float, None]


class Parameter:
    def __init__(self, label: str, datatype: URIRef, default_value: Union[URIRef, LiteralValue]) -> None:
        super().__init__()
        self.label = label
        self.datatype = datatype
        self.default_value = default_value

    @property
    def url_name(self):
        return self.label.replace(' ', '_').replace('-', '_').lower()


class Transformation:
    owl_type = dtbox.Transformation

    def __init__(self, query: str, language: str = 'SPARQL') -> None:
        super().__init__()
        self.language = language
        self.query = query

    def triples(self):
        return [
            (dtbox.transformation_query, Literal(self.query)),
            (dtbox.transformation_language, Literal(self.language))
        ]


class CopyTransformation(Transformation):
    owl_type = dtbox.CopyTransformation

    def __init__(self, input: int, output: int) -> None:
        super().__init__(query=f'COPY input {input} TO output {output}', language='COPY')
        self.input = input
        self.output = output

    def triples(self):
        return super().triples() + [
            (dtbox.copy_input, Literal(self.input)),
            (dtbox.copy_output, Literal(self.output))
        ]


class Implementation:
    def __init__(self, name: str, algorithm: URIRef, parameters: List[Parameter],
                 transformations: List[Transformation],
                 input: List[Union[URIRef, List[URIRef]]] = None, output: List[URIRef] = None,
                 implementation_type=dtbox.Implementation,
                 counterpart: 'Implementation' = None
                 ) -> None:
        super().__init__()
        self.name = name
        self.algorithm = algorithm
        self.parameters = parameters
        self.transformations = transformations
        self.input = input or []
        self.output = output or []
        assert implementation_type in {dtbox.Implementation, dtbox.LearnerImplementation, dtbox.ApplierImplementation}
        self.implementation_type = implementation_type
        self.counterpart = counterpart
        if self.counterpart is not None:
            assert implementation_type in {dtbox.LearnerImplementation, dtbox.ApplierImplementation}
            if self.counterpart.counterpart is None:
                self.counterpart.counterpart = self

    @property
    def url_name(self):
        return self.name.replace(' ', '_').replace('-', '_').lower()

    def add_to_graph(self, g: Graph):
        uri = f'implementation/{self.url_name}'
        implementation_ref = dabox[uri]
        g.add((implementation_ref, RDF.type, self.implementation_type))
        g.add((implementation_ref, RDFS.label, Literal(self.name)))
        g.add((implementation_ref, dtbox.implements, self.algorithm))
        for i, input_tag in enumerate(self.input):
            input_node = BNode()
            g.add((input_node, RDF.type, dtbox.IOSpec))
            g.add((implementation_ref, dtbox.specifiesInput, input_node))
            g.add((input_node, dtbox.has_position, Literal(i)))
            if isinstance(input_tag, list):
                input_collection = BNode()
                input_shape = BNode()
                Collection(g, input_collection, input_tag)
                g.add((input_shape, RDF.type, dtbox.DataTag))
                g.add((input_shape, RDF.type, SH.NodeShape))
                g.add((input_shape, SH['and'], input_collection))
                g.add((input_node, dtbox.hasTag, input_shape))

            else:
                g.add((input_node, dtbox.hasTag, input_tag))
        for i, output_tag in enumerate(self.output):
            output_node = BNode()
            g.add((output_node, RDF.type, dtbox.IOSpec))
            g.add((implementation_ref, dtbox.specifiesOutput, output_node))
            g.add((output_node, dtbox.hasTag, output_tag))
            g.add((output_node, dtbox.has_position, Literal(i)))
        for i, parameter in enumerate(self.parameters):
            param_ref = dabox[f'{uri}/{parameter.url_name}']
            g.add((param_ref, RDF.type, dtbox.Parameter))
            g.add((param_ref, RDFS.label, Literal(parameter.label)))
            g.add((param_ref, dtbox.hasDatatype, parameter.datatype))
            g.add((param_ref, dtbox.has_position, Literal(i)))
            if isinstance(parameter.default_value, URIRef):
                g.add((param_ref, dtbox.hasDefaultValue, parameter.default_value))
            else:
                g.add((param_ref, dtbox.hasDefaultValue, Literal(parameter.default_value)))
            g.add((implementation_ref, dtbox.hasParameter, param_ref))
        transformation_nodes = []
        for transformation in self.transformations:
            trans_ref = BNode()
            g.add((trans_ref, RDF.type, transformation.owl_type))
            for p, o in transformation.triples():
                g.add((trans_ref, p, o))
            transformation_nodes.append(trans_ref)

        g.add((implementation_ref, dtbox.hasTransformation, Collection(g, uri=BNode(), seq=transformation_nodes).uri))

        return implementation_ref

    def add_counterpart_relationship(self, g: Graph):
        if self.counterpart is None:
            return
        counterpart_query = f'''
        PREFIX dtbox: <{dtbox}>
        SELECT ?self ?counterpart
        WHERE {{
            ?self a <{self.implementation_type}> ;
                rdfs:label "{self.name}" .
            ?counterpart a <{self.counterpart.implementation_type}> ;
                rdfs:label "{self.counterpart.name}" .
        }}
        '''
        result = g.query(counterpart_query).bindings
        assert len(result) == 1
        self_node = result[0][Variable('self')]
        relationship = dtbox.hasApplier if self.implementation_type == dtbox.LearnerImplementation else dtbox.hasLearner
        counterpart_node = result[0][Variable('counterpart')]
        g.add((self_node, relationship, counterpart_node))
