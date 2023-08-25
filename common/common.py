from owlrl import DeductiveClosure, OWLRL_Semantics
from rdflib import *

dmop = Namespace('http://www.e-lico.eu/ontologies/dmo/DMOP/DMOP.owl#')
tb = Namespace('https://extremexp.eu/ontology/tbox#')
cb = Namespace('https://extremexp.eu/ontology/cbox#')
ab = Namespace('https://extremexp.eu/ontology/abox#')


def get_graph_xp():
    g = Graph()
    g.bind('tb', tb)
    g.bind('cb', cb)
    g.bind('ab', ab)
    g.bind('dmop', dmop)
    return g


def get_graph():
    g = Graph()
    g.bind('dmop', dmop)
    g.bind('dtbox', do)
    g.bind('dshapes', ds)
    g.bind('dabox', da)
    g.bind('ddata', dd)
    g.bind('dworkflow', dw)
    return g


def get_ontology_graph():
    graph = get_graph_xp()
    ontologies = [
        'C:/Users/Victor/Development/thesis/Ontology/ontologies/tbox.ttl',
        'C:/Users/Victor/Development/thesis/Ontology/ontologies/cbox.ttl',
        'C:/Users/Victor/Development/thesis/Ontology/ontologies/abox.ttl',
        'C:/Users/Victor/Development/thesis/Ontology/dataset_annotator/penguins_annotated.ttl',
        'C:/Users/Victor/Development/thesis/Ontology/dataset_annotator/titanic_annotated.ttl',
    ]
    for o in ontologies:
        graph.parse(o, format="turtle")

    DeductiveClosure(OWLRL_Semantics).expand(graph)
    return graph
