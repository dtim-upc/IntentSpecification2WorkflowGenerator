from ontology_populator.implementations.core import *
from common import *

db_delete_filter = Implementation(
    name='DB Delete (Filter)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Table to delete from', None, None), # TODO: check parameter
        Parameter('Query view', None, None), # TODO: check parameter
        Parameter('Add Condition', None, None), # TODO: check parameter
        Parameter('Group', None, None), # TODO: check parameter
        Parameter('Remove Group', None, None), # TODO: check parameter
        Parameter('Delete', None, None), # TODO: check parameter
        Parameter('Edit condition', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_delete_table = Implementation(
    name='DB Delete (Table)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_insert = Implementation(
    name='DB Insert',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_loader = Implementation(
    name='DB Loader',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_looping = Implementation(
    name='DB Looping',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_merge = Implementation(
    name='DB Merge',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_query_reader = Implementation(
    name='DB Query Reader',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_reader = Implementation(
    name='DB Reader',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_row_manipulator = Implementation(
    name='DB Row Manipulator',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_update = Implementation(
    name='DB Update',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_writer = Implementation(
    name='DB Writer',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

parameterized_db_query_reader = Implementation(
    name='Parameterized DB Query Reader',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
