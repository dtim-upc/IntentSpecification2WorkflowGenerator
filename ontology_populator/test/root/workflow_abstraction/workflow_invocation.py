from ontology_populator.implementations.core import *
from common import *

call_workflow_service = Implementation(
    name='Call Workflow Service',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

workflow_service_input = Implementation(
    name='Workflow Service Input',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

workflow_service_output = Implementation(
    name='Workflow Service Output',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

call_workflow_table_based = Implementation(
    name='Call Workflow (Table Based)',
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

call_workflow_row_based = Implementation(
    name='Call Workflow (Row Based)',
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

container_input_credentials = Implementation(
    name='Container Input (Credentials)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_input_raw_http = Implementation(
    name='Container Input (Raw HTTP)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('File for response body', None, None), # TODO: check parameter
        Parameter('Default headers', None, None), # TODO: check parameter
        Parameter('Default query parameters', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_input_row = Implementation(
    name='Container Input (Row)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Accept any input', None, None), # TODO: check parameter
        Parameter('Require input to match template row specification', None, None), # TODO: check parameter
        Parameter('Template row', None, None), # TODO: check parameter
        Parameter('Set first row of input as template', None, None), # TODO: check parameter
        Parameter('Missing values', None, None), # TODO: check parameter
        Parameter('Missing columns', None, None), # TODO: check parameter
        Parameter('Unknown columns', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_input_table = Implementation(
    name='Container Input (Table)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Template table', None, None), # TODO: check parameter
        Parameter('Set input table as template', None, None), # TODO: check parameter
        Parameter('Use entire input table', None, None), # TODO: check parameter
        Parameter('Use only first rows', None, None), # TODO: check parameter
        Parameter('Omit table spec in API definition', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_input_file = Implementation(
    name='Container Input (File)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Variable name', None, None), # TODO: check parameter
        Parameter('Use a default file', None, None), # TODO: check parameter
        Parameter('Read from', None, None), # TODO: check parameter
        Parameter('File, Folder or URL', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_input_variable = Implementation(
    name='Container Input (Variable)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Accept any input', None, None), # TODO: check parameter
        Parameter('Require input to match template variables specification', None, None), # TODO: check parameter
        Parameter('Template Variables', None, None), # TODO: check parameter
        Parameter('Set input variables as template', None, None), # TODO: check parameter
        Parameter('Use simplified JSON format', None, None), # TODO: check parameter
        Parameter('Add', None, None), # TODO: check parameter
        Parameter('Type', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Value', None, None), # TODO: check parameter
        Parameter('Move/Remove variable', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_output_table = Implementation(
    name='Container Output (Table)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_output_raw_http = Implementation(
    name='Container Output (Raw HTTP)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Status code', None, None), # TODO: check parameter
        Parameter('Body column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_output_row = Implementation(
    name='Container Output (Row)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_output_file = Implementation(
    name='Container Output (File)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('File Path Variable', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
