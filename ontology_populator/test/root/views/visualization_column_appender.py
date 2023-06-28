from ontology_populator.implementations.core import *
from common import *

radar_plot_appender = Implementation(
    name='Radar Plot Appender',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Background color', None, None), # TODO: check parameter
        Parameter('Range color', None, None), # TODO: check parameter
        Parameter('Ribbon color', None, None), # TODO: check parameter
        Parameter('Ribbon color 2', None, None), # TODO: check parameter
        Parameter('Ribbon color 2', None, None), # TODO: check parameter
        Parameter('Fail if any column is missing', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

spark_line_appender = Implementation(
    name='Spark Line Appender',
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
