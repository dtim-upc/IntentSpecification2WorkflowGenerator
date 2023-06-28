from ontology_populator.implementations.core import *
from common import *

add_empty_rows = Implementation(
    name='Add Empty Rows',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of rows in output', None, None), # TODO: check parameter
        Parameter('Fill Data', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

extract_column_header = Implementation(
    name='Extract Column Header',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Use new column names', None, None), # TODO: check parameter
        Parameter('Prefix', None, None), # TODO: check parameter
        Parameter('Output Format for Column Names', None, None), # TODO: check parameter
        Parameter('Selected column type', None, None), # TODO: check parameter
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

insert_column_header = Implementation(
    name='Insert Column Header',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Lookup column', None, None), # TODO: check parameter
        Parameter('Value column', None, None), # TODO: check parameter
        Parameter('Fail if no assignment in dictionary table', None, None), # TODO: check parameter
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

rowid = Implementation(
    name='RowID',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Replace RowID with selected column values', None, None), # TODO: check parameter
        Parameter('New RowID column: ', None, None), # TODO: check parameter
        Parameter('Ensure uniqueness', None, None), # TODO: check parameter
        Parameter('Handle missing values', None, None), # TODO: check parameter
        Parameter('Enable hiliting', None, None), # TODO: check parameter
        Parameter('Create new column with the RowID values', None, None), # TODO: check parameter
        Parameter('New column name: ', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

rule_engine = Implementation(
    name='Rule Engine',
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

rule_engine_dictionary = Implementation(
    name='Rule Engine (Dictionary)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
