from ontology_populator.implementations.core import *
from common import *

inject_variables_data = Implementation(
    name='Inject Variables (Data)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

inject_variables_database = Implementation(
    name='Inject Variables (Database)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.database.DatabasePortObject'
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.database.DatabasePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

extract_variables_data = Implementation(
    name='Extract Variables (Data)',
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

extract_variables_database = Implementation(
    name='Extract Variables (Database)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.database.DatabasePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

table_column_to_variable = Implementation(
    name='Table Column to Variable',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column name', None, None), # TODO: check parameter
        Parameter('Skip missing values', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

table_row_to_variable = Implementation(
    name='Table Row to Variable',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Missing value handling', None, None), # TODO: check parameter
        Parameter('Defaults', None, None), # TODO: check parameter
        Parameter('Column selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

variable_to_table_column = Implementation(
    name='Variable to Table Column',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Variable Selection', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

variable_to_table_row = Implementation(
    name='Variable to Table Row',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Row name', None, None), # TODO: check parameter
        Parameter('Variable Filter', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

java_edit_variable = Implementation(
    name='Java Edit Variable',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Snippet text area', None, None), # TODO: check parameter
        Parameter('Input', None, None), # TODO: check parameter
        Parameter('Output', None, None), # TODO: check parameter
        Parameter('Run script during node configuration or during node execution', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

java_edit_variable_simple = Implementation(
    name='Java Edit Variable (simple)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Method Body', None, None), # TODO: check parameter
        Parameter('Compile on close', None, None), # TODO: check parameter
        Parameter('Return type', None, None), # TODO: check parameter
        Parameter('Overwrite or define new variable', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

math_formula_variable = Implementation(
    name='Math Formula (Variable)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Category', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
        Parameter('Append Variable', None, None), # TODO: check parameter
        Parameter('Replace Variable', None, None), # TODO: check parameter
        Parameter('Convert to Int', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

merge_variables = Implementation(
    name='Merge Variables',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

rule_engine_variable = Implementation(
    name='Rule Engine Variable',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Category', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
        Parameter('New flow variable name', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

rule_engine_variable_dictionary = Implementation(
    name='Rule Engine Variable (Dictionary)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Rules column', None, None), # TODO: check parameter
        Parameter('=>', None, None), # TODO: check parameter
        Parameter('Treat values starting with $ as references', None, None), # TODO: check parameter
        Parameter('Result variable', None, None), # TODO: check parameter
        Parameter('Errors', None, None), # TODO: check parameter
        Parameter('Warnings', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

string_manipulation_variable = Implementation(
    name='String Manipulation (Variable)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
        Parameter('Replace/Append', None, None), # TODO: check parameter
        Parameter('Syntax check on close', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

variable_to_credentials = Implementation(
    name='Variable to Credentials',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Credentials name', None, None), # TODO: check parameter
        Parameter('Username variable', None, None), # TODO: check parameter
        Parameter('Password variable', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
