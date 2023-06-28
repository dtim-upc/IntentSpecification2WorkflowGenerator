from ontology_populator.implementations.core import *
from common import *

association_rule_learner = Implementation(
    name='Association Rule Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column containing transactions', None, None), # TODO: check parameter
        Parameter('Minimum support (0-1)', None, None), # TODO: check parameter
        Parameter('Underlying data structure', None, None), # TODO: check parameter
        Parameter('Itemset type', None, None), # TODO: check parameter
        Parameter('Maximal itemset length', None, None), # TODO: check parameter
        Parameter('Output association rules', None, None), # TODO: check parameter
        Parameter('Minimum confidence', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
