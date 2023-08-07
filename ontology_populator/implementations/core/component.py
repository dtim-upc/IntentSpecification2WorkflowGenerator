from typing import List, Union, Tuple, Any

from rdflib.collection import Collection

from common import *
from .parameter import Parameter
from .transformation import Transformation
from .implementation import Implementation

LiteralValue = Union[str, bool, int, float, None]


class Component:

    def __init__(self, name: str, implementation: Implementation, transformations: List[Transformation],
                 exposed_parameters: List[str] = None,
                 overriden_parameters: List[Tuple[str, Any]] = None,
                 counterpart: Union['Component', List['Component']] = None,
                 namespace: Namespace = dabox) -> None:
        super().__init__()
        self.name = name
        self.url_name = f'component-{self.name.replace(" ", "_").replace("-", "_").lower()}'
        self.uri_ref = namespace[self.url_name]

        self.implementation = implementation
        self.transformations = transformations
        self.overriden_parameters = overriden_parameters if overriden_parameters is not None else []
        self.exposed_parameters = exposed_parameters if exposed_parameters is not None else []
        self.component_type = {
            dtbox.LearnerImplementation: dtbox.LearnerComponent,
            dtbox.ApplierImplementation: dtbox.ApplierComponent,
            dtbox.Implementation: dtbox.Component,
        }[self.implementation.implementation_type]
        self.counterpart = counterpart
        if self.counterpart is not None:
            assert self.component_type in {dtbox.LearnerComponent, dtbox.ApplierComponent}
            if isinstance(self.counterpart, list):
                for c in self.counterpart:
                    if c.counterpart is None:
                        c.counterpart = self
            elif self.counterpart.counterpart is None:
                self.counterpart.counterpart = self

    def add_to_graph(self, g: Graph):

        # Base triples
        g.add((self.uri_ref, RDF.type, self.component_type))
        g.add((self.uri_ref, RDFS.label, Literal(self.name)))
        g.add((self.uri_ref, dtbox.hasImplementation, self.implementation.uri_ref))

        # Transformation triples
        transformation_nodes = []
        for transformation in self.transformations:
            trans_ref = BNode()
            g.add((trans_ref, RDF.type, transformation.owl_type))
            for p, o in transformation.triples():
                g.add((trans_ref, p, o))
            transformation_nodes.append(trans_ref)

        g.add((self.uri_ref, dtbox.hasTransformation, Collection(g, uri=BNode(), seq=transformation_nodes).uri))

        # Overriden parameters triples
        for parameter, value in self.overriden_parameters:
            parameter_value = BNode()
            g.add((parameter_value, RDF.type, dtbox.ParameterValue))
            g.add((parameter_value, dtbox.forParameter, self.implementation.parameters[parameter].uri_ref))
            g.add((parameter_value, dtbox.has_value, Literal(value)))
            g.add((self.uri_ref, dtbox.overridesParameter, parameter_value))

        # Exposed parameters triples
        for parameter in self.exposed_parameters:
            g.add((self.uri_ref, dtbox.exposesParameter, self.implementation.parameters[parameter].uri_ref))

        return self.uri_ref

    def add_counterpart_relationship(self, g: Graph):
        if self.counterpart is None:
            return
        counters = self.counterpart if isinstance(self.counterpart, list) else [self.counterpart]
        for c in counters:
            counterpart_query = f'''
            PREFIX dtbox: <{dtbox}>
            SELECT ?self ?counterpart
            WHERE {{
                ?self a <{self.component_type}> ;
                    rdfs:label "{self.name}" .
                ?counterpart a <{c.component_type}> ;
                    rdfs:label "{c.name}" .
            }}
            '''
            result = g.query(counterpart_query).bindings
            assert len(result) == 1
            self_node = result[0][Variable('self')]
            relationship = dtbox.hasApplier if self.component_type == dtbox.LearnerComponent else dtbox.hasLearner
            counterpart_node = result[0][Variable('counterpart')]
            g.add((self_node, relationship, counterpart_node))
