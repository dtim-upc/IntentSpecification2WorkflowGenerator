from ontology_populator.implementations.core import *
from common import *

interactive_hilite_collector = Implementation(
    name='Interactive HiLite Collector',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Append Annotation', None, None), # TODO: check parameter
        Parameter('Apply', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

table_manipulator = Implementation(
    name='Table Manipulator',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Use existing row ID', None, None), # TODO: check parameter
        Parameter('Prepend table index to row ID', None, None), # TODO: check parameter
        Parameter('Transformations', None, None), # TODO: check parameter
        Parameter('Reset order', None, None), # TODO: check parameter
        Parameter('Reset filter', None, None), # TODO: check parameter
        Parameter('Reset names', None, None), # TODO: check parameter
        Parameter('Reset types', None, None), # TODO: check parameter
        Parameter('Reset all', None, None), # TODO: check parameter
        Parameter('Enforce types', None, None), # TODO: check parameter
        Parameter('Take columns from', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

table_validator = Implementation(
    name='Table Validator',
    algorithm=None, # TODO: check algorithm
    parameters=[
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

table_validator_reference = Implementation(
    name='Table Validator (Reference)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
