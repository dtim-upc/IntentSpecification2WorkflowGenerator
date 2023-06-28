from ontology_populator.implementations.core import *
from common import *

gradient_boosted_trees_to_pmml = Implementation(
    name='Gradient Boosted Trees to PMML',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.treeensemble2.model.GradientBoostingModelPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
