from typing import List, Union, Optional

from common import *
from ontology_populator.implementations.core import Implementation, Parameter
from ontology_populator.implementations.core.parameter import LiteralValue


class KnimeImplementation(Implementation):

    def __init__(self, name: str, algorithm: URIRef, parameters: List[Parameter],
                 knime_node_factory: str, knime_bundle: 'KnimeBundle',
                 input: List[Union[URIRef, List[URIRef]]] = None, output: List[URIRef] = None,
                 implementation_type=dtbox.Implementation, counterpart: 'Implementation' = None,
                 ) -> None:
        super().__init__(name, algorithm, parameters, input, output, implementation_type, counterpart)
        self.knime_node_factory = knime_node_factory
        self.knime_bundle = knime_bundle

    def add_to_graph(self, g: Graph):
        super().add_to_graph(g)
        g.add((self.uri_ref, dtbox.knime_node_factory, Literal(self.knime_node_factory)))
        g.add((self.uri_ref, dtbox.knime_bundle_name, Literal(self.knime_bundle.name)))
        g.add((self.uri_ref, dtbox.knime_bundle_symbolic_name, Literal(self.knime_bundle.symbolic_name)))
        g.add((self.uri_ref, dtbox.knime_bundle_vendor, Literal(self.knime_bundle.vendor)))
        g.add((self.uri_ref, dtbox.engine, Literal('KNIME')))

        for parameter in self.parameters:
            if isinstance(parameter, KnimeParameter):
                g.add((parameter.uri_ref, dtbox.knime_key, Literal(parameter.knime_key)))
                g.add((parameter.uri_ref, dtbox.knime_path, Literal(parameter.path)))

        return self.uri_ref


class KnimeParameter(Parameter):

    def __init__(self, label: str, datatype: URIRef, default_value: Union[URIRef, LiteralValue],
                 knime_key: str, path: str = 'model') -> None:
        super().__init__(label, datatype, default_value)
        self.knime_key = knime_key
        self.path = path


class KnimeBundle:

    def __init__(self, name: str, symbolic_name: str, vendor: str) -> None:
        super().__init__()
        self.name = name
        self.symbolic_name = symbolic_name
        self.vendor = vendor


KnimeBaseBundle = KnimeBundle('KNIME Base Bundle', 'org.knime.base', 'KNIME AG, Zurich, Switzerland')
