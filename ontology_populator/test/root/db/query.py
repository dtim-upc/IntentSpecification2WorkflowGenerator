from ontology_populator.implementations.core import *
from common import *

db_apply-binner = Implementation(
    name='DB Apply-Binner',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

db_auto-binner = Implementation(
    name='DB Auto-Binner',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

db_column_filter = Implementation(
    name='DB Column Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_column_rename = Implementation(
    name='DB Column Rename',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Search', None, None), # TODO: check parameter
        Parameter('Filter Options', None, None), # TODO: check parameter
        Parameter('Change', None, None), # TODO: check parameter
        Parameter('Remove', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_column_rename_regex = Implementation(
    name='DB Column Rename (Regex)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Search String (regexp)', None, None), # TODO: check parameter
        Parameter('Replacement', None, None), # TODO: check parameter
        Parameter('Case Insensitive', None, None), # TODO: check parameter
        Parameter('Literal', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_concatenate = Implementation(
    name='DB Concatenate',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Use union of columns', None, None), # TODO: check parameter
        Parameter('Use intersection of columns', None, None), # TODO: check parameter
        Parameter('Remove duplicate rows', None, None), # TODO: check parameter
        Parameter('Keep all rows', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_groupby = Implementation(
    name='DB GroupBy',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_joiner = Implementation(
    name='DB Joiner',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_numeric-binner = Implementation(
    name='DB Numeric-Binner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select Column: ', None, None), # TODO: check parameter
        Parameter('Append new column: ', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

db_partitioning = Implementation(
    name='DB Partitioning',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Absolute', None, None), # TODO: check parameter
        Parameter('Relative', None, None), # TODO: check parameter
        Parameter('Take from top', None, None), # TODO: check parameter
        Parameter('Draw randomly', None, None), # TODO: check parameter
        Parameter('Stratified sampling', None, None), # TODO: check parameter
        Parameter('Random seed', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_pivot = Implementation(
    name='DB Pivot',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_query = Implementation(
    name='DB Query',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('SQL Statement', None, None), # TODO: check parameter
        Parameter('Database Metadata Browser', None, None), # TODO: check parameter
        Parameter('Database Column List', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Preview', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_row_filter = Implementation(
    name='DB Row Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Preview', None, None), # TODO: check parameter
        Parameter('Add Condition', None, None), # TODO: check parameter
        Parameter('Group', None, None), # TODO: check parameter
        Parameter('Ungroup', None, None), # TODO: check parameter
        Parameter('Delete', None, None), # TODO: check parameter
        Parameter('Edit condition', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_row_sampling = Implementation(
    name='DB Row Sampling',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Absolute', None, None), # TODO: check parameter
        Parameter('Relative', None, None), # TODO: check parameter
        Parameter('Take from top', None, None), # TODO: check parameter
        Parameter('Draw randomly', None, None), # TODO: check parameter
        Parameter('Stratified sampling', None, None), # TODO: check parameter
        Parameter('Random seed', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_sorter = Implementation(
    name='DB Sorter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Add columns', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBDataPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_table_selector = Implementation(
    name='DB Table Selector',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Schema', None, None), # TODO: check parameter
        Parameter('Table', None, None), # TODO: check parameter
        Parameter('Select a table', None, None), # TODO: check parameter
        Parameter('Custom Query', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('SQL Statement', None, None), # TODO: check parameter
        Parameter('Preview', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBDataPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
