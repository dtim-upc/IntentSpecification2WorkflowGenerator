from typing import List

from rdflib.term import Node

from common import *

from pipeline_generator.pipeline_generator import *


def abstract_planner(ontology: Graph, intent: Graph) -> List[Dict[Node, List[Node]]]:
    dataset, problem, intent_params, intent_iri = get_intent_info(intent)

    impls = get_potential_implementations(ontology, problem, [])

    algs = [(next(ontology.objects(impl[0], tb.implements)),
             (impl[0], RDF.type, tb.LearnerImplementation) in ontology) for impl in impls]

    plans = []
    for alg, train in algs:
        if train:
            trainer = cb.term(alg.fragment + '-Train')
            plans.append({
                cb.DataLoading: [cb.Partitioning],
                cb.Partitioning: [trainer, alg],
                trainer: [alg],
                alg: [],
            })
        else:
            plans.append({
                cb.DataLoading: [alg],
                alg: [],
            })

    return plans


if __name__ == '__main__':
    intent_graph = get_graph_xp()
    intent = 'D'
    data = 'titanic.csv'
    problem = 'Description'
    intent_graph.add((ab.term(intent), RDF.type, tb.Intent))
    intent_graph.add((ab.term(intent), tb.overData, ab.term(data)))
    intent_graph.add((ab.term(intent), tb.tackles, cb.term(problem)))

    abstract_plans = abstract_planner(get_ontology_graph(), intent_graph)
    print(abstract_plans)
