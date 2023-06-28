from ontology_populator.implementations.core import *
from common import *

correlation_filter = Implementation(
    name='Correlation Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Columns from Model', None, None), # TODO: check parameter
        Parameter('Correlation Threshold', None, None), # TODO: check parameter
        Parameter('Calculate', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.preproc.correlation.pmcc.PMCCPortObjectAndSpec'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

low_variance_filter = Implementation(
    name='Low Variance Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

feature_selection_loop_start_1:1 = Implementation(
    name='Feature Selection Loop Start (1:1)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

feature_selection_loop_start_2:2 = Implementation(
    name='Feature Selection Loop Start (2:2)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

feature_selection_loop_end = Implementation(
    name='Feature Selection Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Score variable', None, None), # TODO: check parameter
        Parameter('Minimize', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.base.node.meta.feature.selection.FeatureSelectionModel'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

feature_selection_filter = Implementation(
    name='Feature Selection Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Include static columns', None, None), # TODO: check parameter
        Parameter('Select features manually', None, None), # TODO: check parameter
        Parameter('Select best score', None, None), # TODO: check parameter
        Parameter('Select features automatically by score threshold', None, None), # TODO: check parameter
        Parameter('Prediction score threshold', None, None), # TODO: check parameter
        Parameter('Feature set table', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.meta.feature.selection.FeatureSelectionModel'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
