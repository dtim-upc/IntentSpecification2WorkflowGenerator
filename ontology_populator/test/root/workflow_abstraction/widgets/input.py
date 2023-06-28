from ontology_populator.implementations.core import *
from common import *

boolean_widget = Implementation(
    name='Boolean Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

credentials_widget = Implementation(
    name='Credentials Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Username', None, None), # TODO: check parameter
        Parameter('Password', None, None), # TODO: check parameter
        Parameter('Prompt user name in widget view', None, None), # TODO: check parameter
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

date&time_widget = Implementation(
    name='Date&Time Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('"Now" Button in Wizard', None, None), # TODO: check parameter
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

double_widget = Implementation(
    name='Double Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
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

file_chooser_widget = Implementation(
    name='File Chooser Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
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

file_upload_widget = Implementation(
    name='File Upload Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Valid File Extensions', None, None), # TODO: check parameter
        Parameter('Default File', None, None), # TODO: check parameter
        Parameter('Timeout', None, None), # TODO: check parameter
        Parameter('Disable output, if file does not exist', None, None), # TODO: check parameter
        Parameter('Store uploaded file in workflow directory', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

integer_widget = Implementation(
    name='Integer Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
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

list_box_widget = Implementation(
    name='List Box Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
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

molecule_widget = Implementation(
    name='Molecule Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Hide in Dialog', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Enable SMILES, SMARTS, HELM Formats', None, None), # TODO: check parameter
        Parameter('Format', None, None), # TODO: check parameter
        Parameter('Default Value', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

slider_widget = Implementation(
    name='Slider Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

string_widget = Implementation(
    name='String Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Editor type', None, None), # TODO: check parameter
        Parameter('Multi-line editor width', None, None), # TODO: check parameter
        Parameter('Multi-line editor height', None, None), # TODO: check parameter
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

autocomplete_text_widget = Implementation(
    name='Autocomplete Text Widget',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
