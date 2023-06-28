from ontology_populator.implementations.core import *
from common import *

container_input_json = Implementation(
    name='Container Input (JSON)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('JSON', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

container_output_json = Implementation(
    name='Container Output (JSON)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Append unique ID to parameter name', None, None), # TODO: check parameter
        Parameter('JSON Column', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Keep single-row tables simple', None, None), # TODO: check parameter
        Parameter('Example', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_reader = Implementation(
    name='JSON Reader',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_writer = Implementation(
    name='JSON Writer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Write to', None, None), # TODO: check parameter
        Parameter('Folder', None, None), # TODO: check parameter
        Parameter('Create missing folders', None, None), # TODO: check parameter
        Parameter('If exists', None, None), # TODO: check parameter
        Parameter('JSON', None, None), # TODO: check parameter
        Parameter('File names', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

string_to_json = Implementation(
    name='String to JSON',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Input column', None, None), # TODO: check parameter
        Parameter('Replace', None, None), # TODO: check parameter
        Parameter('Append', None, None), # TODO: check parameter
        Parameter('Allow comments', None, None), # TODO: check parameter
        Parameter('Fail on error', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

table_to_json = Implementation(
    name='Table to JSON',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Input columns', None, None), # TODO: check parameter
        Parameter('Row keys|Omit row key', None, None), # TODO: check parameter
        Parameter('Row keys|Row key as JSON key', None, None), # TODO: check parameter
        Parameter('Row keys|Row key as JSON value with key', None, None), # TODO: check parameter
        Parameter('Row-oriented', None, None), # TODO: check parameter
        Parameter('Column-oriented', None, None), # TODO: check parameter
        Parameter('Keep rows', None, None), # TODO: check parameter
        Parameter('Remove source columns', None, None), # TODO: check parameter
        Parameter('Column names as paths, where path separator in column names', None, None), # TODO: check parameter
        Parameter('Missing values are omitted', None, None), # TODO: check parameter
        Parameter('Missing values are inserted as 'null'', None, None), # TODO: check parameter
        Parameter('Output column name', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_to_table = Implementation(
    name='JSON to Table',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Input JSON column', None, None), # TODO: check parameter
        Parameter('Remove source column', None, None), # TODO: check parameter
        Parameter('Use path with separator', None, None), # TODO: check parameter
        Parameter('Use leaf name (uniquify with (#1)/(#2)/...)', None, None), # TODO: check parameter
        Parameter('Arrays|Keep as JSON array', None, None), # TODO: check parameter
        Parameter('Arrays|Keep as collection elements', None, None), # TODO: check parameter
        Parameter('Arrays|Expand to columns', None, None), # TODO: check parameter
        Parameter('Only leaves', None, None), # TODO: check parameter
        Parameter('Only up to level', None, None), # TODO: check parameter
        Parameter('Omit nested objects', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

columns_to_json = Implementation(
    name='Columns to JSON',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('Unnamed root element', None, None), # TODO: check parameter
        Parameter('Custom key', None, None), # TODO: check parameter
        Parameter('Data bound key', None, None), # TODO: check parameter
        Parameter('Manual selection', None, None), # TODO: check parameter
        Parameter('Automatic selection', None, None), # TODO: check parameter
        Parameter('Custom key/value pairs', None, None), # TODO: check parameter
        Parameter('Remove source columns', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

xml_to_json = Implementation(
    name='XML To JSON',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Input column', None, None), # TODO: check parameter
        Parameter('Replace input column', None, None), # TODO: check parameter
        Parameter('Append new column', None, None), # TODO: check parameter
        Parameter('Text body translated to JSON with key', None, None), # TODO: check parameter
        Parameter('Translate comments', None, None), # TODO: check parameter
        Parameter('Translate processing instructions', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_to_xml = Implementation(
    name='JSON To XML',
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

json_path = Implementation(
    name='JSON Path',
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

json_path_dictionary = Implementation(
    name='JSON Path (Dictionary)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('JSON column', None, None), # TODO: check parameter
        Parameter('Remove source column', None, None), # TODO: check parameter
        Parameter('JSONPath', None, None), # TODO: check parameter
        Parameter('Type of column', None, None), # TODO: check parameter
        Parameter('Output name', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_column_combiner = Implementation(
    name='JSON Column Combiner',
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

json_row_combiner = Implementation(
    name='JSON Row Combiner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('JSON column', None, None), # TODO: check parameter
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('Omit root', None, None), # TODO: check parameter
        Parameter('Add root object with key', None, None), # TODO: check parameter
        Parameter('Custom key/value pairs', None, None), # TODO: check parameter
        Parameter('Collect into array', None, None), # TODO: check parameter
        Parameter('Collect into object with key', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_row_combiner_and_writer = Implementation(
    name='JSON Row Combiner and Writer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('JSON column', None, None), # TODO: check parameter
        Parameter('Output file', None, None), # TODO: check parameter
        Parameter('Overwrite existing file', None, None), # TODO: check parameter
        Parameter('Pretty print', None, None), # TODO: check parameter
        Parameter('Omit root', None, None), # TODO: check parameter
        Parameter('Add root object with key', None, None), # TODO: check parameter
        Parameter('Custom key/value pairs', None, None), # TODO: check parameter
        Parameter('Collect into array', None, None), # TODO: check parameter
        Parameter('Collect into object with key', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_transformer = Implementation(
    name='JSON Transformer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('JSON column', None, None), # TODO: check parameter
        Parameter('Remove source column', None, None), # TODO: check parameter
        Parameter('New column', None, None), # TODO: check parameter
        Parameter('Patch type', None, None), # TODO: check parameter
        Parameter('Keep original value when 'test' operation fails', None, None), # TODO: check parameter
        Parameter('Patch', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_schema_validator = Implementation(
    name='JSON Schema Validator',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('JSON column', None, None), # TODO: check parameter
        Parameter('Schema', None, None), # TODO: check parameter
        Parameter('Fail on invalid JSON value', None, None), # TODO: check parameter
        Parameter('Error message column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

json_diff = Implementation(
    name='JSON Diff',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Source (JSON) column', None, None), # TODO: check parameter
        Parameter('Target (JSON) column', None, None), # TODO: check parameter
        Parameter('Remove source column', None, None), # TODO: check parameter
        Parameter('New column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
