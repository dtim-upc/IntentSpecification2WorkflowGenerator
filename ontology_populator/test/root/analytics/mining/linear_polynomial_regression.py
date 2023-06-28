from ontology_populator.implementations.core import *
from common import *

linear_regression_learner = Implementation(
    name='Linear Regression Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Target', None, None), # TODO: check parameter
        Parameter('Values', None, None), # TODO: check parameter
        Parameter('Predefined Offset Value', None, None), # TODO: check parameter
        Parameter('Missing Values in Input Data', None, None), # TODO: check parameter
        Parameter('Scatter Plot View', None, None), # TODO: check parameter
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

polynomial_regression_learner = Implementation(
    name='Polynomial Regression Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

regression_predictor = Implementation(
    name='Regression Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Custom prediction column name', None, None), # TODO: check parameter
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
