from ontology_populator.implementations.core import *
from common import *

svm_learner = Implementation(
    name='SVM Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Class column', None, None), # TODO: check parameter
        Parameter('Overlapping penalty', None, None), # TODO: check parameter
        Parameter('Kernel type', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

svm_predictor = Implementation(
    name='SVM Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Prediction column', None, None), # TODO: check parameter
        Parameter('Append Class Columns', None, None), # TODO: check parameter
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
