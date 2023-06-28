from ontology_populator.implementations.core import *
from common import *

multilayerperceptron_predictor = Implementation(
    name='MultiLayerPerceptron Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Prediction Column', None, None), # TODO: check parameter
        Parameter('Append columns with class probabilities', None, None), # TODO: check parameter
        Parameter('Suffix for probability columns', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

rprop_mlp_learner = Implementation(
    name='RProp MLP Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Maximum number of iterations', None, None), # TODO: check parameter
        Parameter('Number of hidden layers', None, None), # TODO: check parameter
        Parameter('Number of hidden neurons per layer', None, None), # TODO: check parameter
        Parameter('Class column', None, None), # TODO: check parameter
        Parameter('Ignore missing values', None, None), # TODO: check parameter
        Parameter('Use seed for random initialization', None, None), # TODO: check parameter
        Parameter('Random seed', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
