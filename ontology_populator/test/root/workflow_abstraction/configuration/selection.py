from ontology_populator.implementations.core import *
from common import *

column_filter_configuration = Implementation(
    name='Column Filter Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Type Filter', None, None), # TODO: check parameter
        Parameter('Validation', None, None), # TODO: check parameter
        Parameter('Default Values', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

column_selection_configuration = Implementation(
    name='Column Selection Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
        Parameter('Type Filter', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

multiple_selection_configuration = Implementation(
    name='Multiple Selection Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
        Parameter('Possible Choices', None, None), # TODO: check parameter
        Parameter('Default Values', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

nominal_row_filter_configuration = Implementation(
    name='Nominal Row Filter Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
        Parameter('Lock Column', None, None), # TODO: check parameter
        Parameter('Default Column', None, None), # TODO: check parameter
        Parameter('Default Values', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

single_selection_configuration = Implementation(
    name='Single Selection Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
        Parameter('Possible Choices', None, None), # TODO: check parameter
        Parameter('Default Values', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

value_selection_configuration = Implementation(
    name='Value Selection Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
        Parameter('Lock Column', None, None), # TODO: check parameter
        Parameter('Default Column', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
