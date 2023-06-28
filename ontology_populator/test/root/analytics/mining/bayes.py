from ontology_populator.implementations.core import *
from common import *

naive_bayes_learner = Implementation(
    name='Naive Bayes Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Classification Column', None, None), # TODO: check parameter
        Parameter('Default probability', None, None), # TODO: check parameter
        Parameter('Minimum standard deviation', None, None), # TODO: check parameter
        Parameter('Threshold standard deviation', None, None), # TODO: check parameter
        Parameter('Maximum number of unique nominal values per attribute', None, None), # TODO: check parameter
        Parameter('Ignore missing values', None, None), # TODO: check parameter
        Parameter('Create PMML 4.2 compatible model', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

naive_bayes_predictor = Implementation(
    name='Naive Bayes Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Append columns with normalized class distribution', None, None), # TODO: check parameter
        Parameter('Suffix for probability columns', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
