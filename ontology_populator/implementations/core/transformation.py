from typing import Union

from common import *

LiteralValue = Union[str, bool, int, float, None]


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


class LoaderTransformation(Transformation):
    owl_type = dtbox.LoaderTransformation

    def __init__(self) -> None:
        super().__init__(query=f'Set dataset AS output ', language='LOADER')
