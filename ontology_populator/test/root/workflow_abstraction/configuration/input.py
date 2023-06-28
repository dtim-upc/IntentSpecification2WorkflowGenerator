from ontology_populator.implementations.core import *
from common import *

boolean_configuration = Implementation(
    name='Boolean Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
        Parameter('Output as Integer', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

credentials_configuration = Implementation(
    name='Credentials Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Username', None, None), # TODO: check parameter
        Parameter('Password', None, None), # TODO: check parameter
        Parameter('Prompt user name in component dialog', None, None), # TODO: check parameter
        Parameter('Save password in configuration (weakly encrypted)', None, None), # TODO: check parameter
        Parameter('Use KNIME Server Login (when run on server)', None, None), # TODO: check parameter
        Parameter('Don't render input fields', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

date&time_configuration = Implementation(
    name='Date&Time Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Granularity in Wizard', None, None), # TODO: check parameter
        Parameter('Type', None, None), # TODO: check parameter
        Parameter('Earliest', None, None), # TODO: check parameter
        Parameter('Latest', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

double_configuration = Implementation(
    name='Double Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Minimum', None, None), # TODO: check parameter
        Parameter('Maximum', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

integer_configuration = Implementation(
    name='Integer Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Minimum', None, None), # TODO: check parameter
        Parameter('Maximum', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

integer_slider_configuration = Implementation(
    name='Integer Slider Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Minimum', None, None), # TODO: check parameter
        Parameter('Maximum', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

list_box_configuration = Implementation(
    name='List Box Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Separator', None, None), # TODO: check parameter
        Parameter('Separate at each character', None, None), # TODO: check parameter
        Parameter('Omit Empty Values', None, None), # TODO: check parameter
        Parameter('Regular Expression', None, None), # TODO: check parameter
        Parameter('Validation Error Message', None, None), # TODO: check parameter
        Parameter('Common Regular Expressions', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

local_file_browser_configuration = Implementation(
    name='Local File Browser Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Valid File Extensions', None, None), # TODO: check parameter
        Parameter('Default File', None, None), # TODO: check parameter
        Parameter('Timeout', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

repository_file_chooser_configuration = Implementation(
    name='Repository File Chooser Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Types', None, None), # TODO: check parameter
        Parameter('Output selected item type', None, None), # TODO: check parameter
        Parameter('Valid File Extensions', None, None), # TODO: check parameter
        Parameter('Allow multiple selection', None, None), # TODO: check parameter
        Parameter('Use default mount id of target', None, None), # TODO: check parameter
        Parameter('Custom mount id', None, None), # TODO: check parameter
        Parameter('Root Path', None, None), # TODO: check parameter
        Parameter('Default File', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

string_configuration = Implementation(
    name='String Configuration',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Editor type', None, None), # TODO: check parameter
        Parameter('Editor width', None, None), # TODO: check parameter
        Parameter('Editor height', None, None), # TODO: check parameter
        Parameter('Regular Expression', None, None), # TODO: check parameter
        Parameter('Validation Error Message', None, None), # TODO: check parameter
        Parameter('Common Regular Expressions', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
