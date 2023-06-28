from ontology_populator.implementations.core import *
from common import *

db_connection_table_writer = Implementation(
    name='DB Connection Table Writer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Schema', None, None), # TODO: check parameter
        Parameter('Table', None, None), # TODO: check parameter
        Parameter('Select a table', None, None), # TODO: check parameter
        Parameter('If table exists...', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_data_spec_extractor = Implementation(
    name='DB Data Spec Extractor',
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

db_query_extractor = Implementation(
    name='DB Query Extractor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable with SQL Query', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_query_injector = Implementation(
    name='DB Query Injector',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable with SQL Query', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_sql_executor = Implementation(
    name='DB SQL Executor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('SQL Statement', None, None), # TODO: check parameter
        Parameter('Database Metadata Browser', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Support multiple SQL statements', None, None), # TODO: check parameter
        Parameter('SQL Statement separator', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_table_creator = Implementation(
    name='DB Table Creator',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_table_remover = Implementation(
    name='DB Table Remover',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Schema', None, None), # TODO: check parameter
        Parameter('Table', None, None), # TODO: check parameter
        Parameter('Select a table', None, None), # TODO: check parameter
        Parameter('Cascade', None, None), # TODO: check parameter
        Parameter('Fail if table does not exist', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_type_mapper = Implementation(
    name='DB Type Mapper',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Mapping by Name', None, None), # TODO: check parameter
        Parameter('Mapping by Type', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
