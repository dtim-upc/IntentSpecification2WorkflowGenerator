from ontology_populator.implementations.core import *
from common import *

db_connection_closer = Implementation(
    name='DB Connection Closer',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_connection_extractor = Implementation(
    name='DB Connection Extractor',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_connector = Implementation(
    name='DB Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

h2_connector = Implementation(
    name='H2 Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

microsoft_access_connector = Implementation(
    name='Microsoft Access Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

microsoft_sql_server_connector = Implementation(
    name='Microsoft SQL Server Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

mysql_connector = Implementation(
    name='MySQL Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

oracle_connector = Implementation(
    name='Oracle Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

postgresql_connector = Implementation(
    name='PostgreSQL Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

sqlite_connector = Implementation(
    name='SQLite Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

vertica_connector = Implementation(
    name='Vertica Connector',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
