from ontology_populator.implementations.core import *
from common import *

box_plot_local = Implementation(
    name='Box Plot (local)',
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

conditional_box_plot_local = Implementation(
    name='Conditional Box Plot (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Nominal Column', None, None), # TODO: check parameter
        Parameter('Numeric Column', None, None), # TODO: check parameter
        Parameter('Show missing values', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

hilite_table_local = Implementation(
    name='HiLite Table (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Clear HiLiting', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

histogram_local = Implementation(
    name='Histogram (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Display all rows', None, None), # TODO: check parameter
        Parameter('No. of rows to display', None, None), # TODO: check parameter
        Parameter('Binning column', None, None), # TODO: check parameter
        Parameter('Aggregation column', None, None), # TODO: check parameter
        Parameter('Number of bins', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

interactive_histogram_local = Implementation(
    name='Interactive Histogram (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Display all rows', None, None), # TODO: check parameter
        Parameter('No. of rows to display: ', None, None), # TODO: check parameter
        Parameter('Binning column: ', None, None), # TODO: check parameter
        Parameter('Aggregation column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

interactive_pie_chart_local = Implementation(
    name='Interactive Pie chart (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Display all rows', None, None), # TODO: check parameter
        Parameter('No. of rows to display: ', None, None), # TODO: check parameter
        Parameter('Pie column: ', None, None), # TODO: check parameter
        Parameter('Aggregation method: ', None, None), # TODO: check parameter
        Parameter('Aggregation column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

interactive_table_local = Implementation(
    name='Interactive Table (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

lift_chart_local = Implementation(
    name='Lift Chart (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column containing true labels', None, None), # TODO: check parameter
        Parameter('Response Label', None, None), # TODO: check parameter
        Parameter('Column containing score (probabilities)', None, None), # TODO: check parameter
        Parameter('Interval width in %', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

line_plot_local = Implementation(
    name='Line Plot (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Nr. of rows to display', None, None), # TODO: check parameter
        Parameter('Ignore columns with more nominal values than:', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

parallel_coordinates_local = Implementation(
    name='Parallel Coordinates (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Nr. of rows to display', None, None), # TODO: check parameter
        Parameter('Ignore columns with more nominal values than:', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

pie_chart_local = Implementation(
    name='Pie chart (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Display all rows', None, None), # TODO: check parameter
        Parameter('No. of rows to display: ', None, None), # TODO: check parameter
        Parameter('Pie column: ', None, None), # TODO: check parameter
        Parameter('Aggregation method: ', None, None), # TODO: check parameter
        Parameter('Aggregation column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

scatter_matrix_local = Implementation(
    name='Scatter Matrix (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Nr. of rows to display', None, None), # TODO: check parameter
        Parameter('Ignore columns with more nominal values than:', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

scatter_plot_local = Implementation(
    name='Scatter Plot (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Nr. of rows to display', None, None), # TODO: check parameter
        Parameter('Ignore columns with more nominal values than:', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
