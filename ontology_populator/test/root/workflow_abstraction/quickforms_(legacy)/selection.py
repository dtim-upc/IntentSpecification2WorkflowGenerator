from ontology_populator.implementations.core import *
from common import *

column_selection_legacy = Implementation(
    name='Column Selection (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Hide in Dialog', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
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

multiple_selections_legacy = Implementation(
    name='Multiple Selections (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Hide in Dialog', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
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

single_selection_legacy = Implementation(
    name='Single Selection (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Hide in Dialog', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
        Parameter('Possible Choices', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
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

value_selection_legacy = Implementation(
    name='Value Selection (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Hide in Dialog', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
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
