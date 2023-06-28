from ontology_populator.implementations.core import *
from common import *

boosting_learner_loop_end = Implementation(
    name='Boosting Learner Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Real class column', None, None), # TODO: check parameter
        Parameter('Predicted class column', None, None), # TODO: check parameter
        Parameter('Number of iterations', None, None), # TODO: check parameter
        Parameter('Use seed for random numbers', None, None), # TODO: check parameter
        Parameter('Seed', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.PortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

boosting_learner_loop_start = Implementation(
    name='Boosting Learner Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

boosting_predictor_loop_end = Implementation(
    name='Boosting Predictor Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Prediction column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

boosting_predictor_loop_start = Implementation(
    name='Boosting Predictor Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Model column', None, None), # TODO: check parameter
        Parameter('Model weight column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.PortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

cell_to_model = Implementation(
    name='Cell To Model',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select the model column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.PortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

model_loop_end = Implementation(
    name='Model Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.PortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

model_loop_start = Implementation(
    name='Model Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.PortObject'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

model_to_cell = Implementation(
    name='Model to Cell',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Row Identifier', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.PortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

prediction_fusion = Implementation(
    name='Prediction Fusion',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Method', None, None), # TODO: check parameter
        Parameter('Classes', None, None), # TODO: check parameter
        Parameter('Class confidences', None, None), # TODO: check parameter
        Parameter('Weight', None, None), # TODO: check parameter
        Parameter('Add prediction', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

voting_loop_end = Implementation(
    name='Voting Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select the winner column', None, None), # TODO: check parameter
        Parameter('Remove individual predictions', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
