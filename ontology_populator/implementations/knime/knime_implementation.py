from typing import List, Union

from common import *
from ontology_populator.implementations.core import Implementation, Parameter


class KnimeImplementation(Implementation):

    def __init__(self, name: str, algorithm: URIRef, parameters: List[Parameter],
                 knime_node_name: str, knime_node_type: str, knime_class: str,
                 input: List[Union[URIRef, List[URIRef]]] = None, output: List[URIRef] = None,
                 implementation_type=dtbox.Implementation, counterpart: 'Implementation' = None,
                 ) -> None:
        super().__init__(name, algorithm, parameters, input, output, implementation_type, counterpart)
        self.knime_node_name = knime_node_name
        self.knime_node_type = knime_node_type
        self.knime_class = knime_class

    def add_to_graph(self, g: Graph):
        super().add_to_graph(g)
        g.add((self.uri_ref, dtbox.knime_identifier, Literal(self.knime_identifier)))
        g.add((self.uri_ref, dtbox.engine, Literal('KNIME')))
        return self.uri_ref
