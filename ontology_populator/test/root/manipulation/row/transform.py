from ontology_populator.implementations.core import *
from common import *

concatenate = Implementation(
    name='Concatenate',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Skip Rows', None, None), # TODO: check parameter
        Parameter('Append suffix', None, None), # TODO: check parameter
        Parameter('Fail', None, None), # TODO: check parameter
        Parameter('Use intersection of columns', None, None), # TODO: check parameter
        Parameter('Use union of columns', None, None), # TODO: check parameter
        Parameter('Enable hiliting', None, None), # TODO: check parameter
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

groupby = Implementation(
    name='GroupBy',
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

ungroup = Implementation(
    name='Ungroup',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Collection columns', None, None), # TODO: check parameter
        Parameter('Remove selected collection column', None, None), # TODO: check parameter
        Parameter('Skip missing values', None, None), # TODO: check parameter
        Parameter('Skip empty collections', None, None), # TODO: check parameter
        Parameter('Enable hiliting', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

partitioning = Implementation(
    name='Partitioning',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Absolute', None, None), # TODO: check parameter
        Parameter('Relative', None, None), # TODO: check parameter
        Parameter('Take from top', None, None), # TODO: check parameter
        Parameter('Linear sampling', None, None), # TODO: check parameter
        Parameter('Draw randomly', None, None), # TODO: check parameter
        Parameter('Stratified sampling', None, None), # TODO: check parameter
        Parameter('Use random seed', None, None), # TODO: check parameter
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

pivoting = Implementation(
    name='Pivoting',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

unpivoting = Implementation(
    name='Unpivoting',
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

rank = Implementation(
    name='Rank',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Ranking Attributes', None, None), # TODO: check parameter
        Parameter('Grouping Attributes', None, None), # TODO: check parameter
        Parameter('Ranking Mode', None, None), # TODO: check parameter
        Parameter('Name of Rank Attribute', None, None), # TODO: check parameter
        Parameter('Retain Row Order', None, None), # TODO: check parameter
        Parameter('Rank as Long', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

row_sampling = Implementation(
    name='Row Sampling',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Absolute', None, None), # TODO: check parameter
        Parameter('Relative', None, None), # TODO: check parameter
        Parameter('Take from top', None, None), # TODO: check parameter
        Parameter('Linear sampling', None, None), # TODO: check parameter
        Parameter('Draw randomly', None, None), # TODO: check parameter
        Parameter('Stratified sampling', None, None), # TODO: check parameter
        Parameter('Use random seed', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

bootstrap_sampling = Implementation(
    name='Bootstrap Sampling',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Sample size in %', None, None), # TODO: check parameter
        Parameter('Absolute sample size', None, None), # TODO: check parameter
        Parameter('Use random seed', None, None), # TODO: check parameter
        Parameter('Append count of occurrences', None, None), # TODO: check parameter
        Parameter('Append original RowID', None, None), # TODO: check parameter
        Parameter('RowID separator', None, None), # TODO: check parameter
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

equal_size_sampling = Implementation(
    name='Equal Size Sampling',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Nominal Column', None, None), # TODO: check parameter
        Parameter('Use exact sampling', None, None), # TODO: check parameter
        Parameter('Use approximate sampling', None, None), # TODO: check parameter
        Parameter('Enable static seed', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

shuffle = Implementation(
    name='Shuffle',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Seed', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

sorter = Implementation(
    name='Sorter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Add sorting criterion', None, None), # TODO: check parameter
        Parameter('Sort in memory', None, None), # TODO: check parameter
        Parameter('Move Missing Cells to end of sorted list', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

top_k_selector = Implementation(
    name='Top k Selector',
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
