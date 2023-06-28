from ontology_populator.implementations.core import *
from common import *

date_field_extractor_legacy = Implementation(
    name='Date Field Extractor (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column containing dates', None, None), # TODO: check parameter
        Parameter('Year', None, None), # TODO: check parameter
        Parameter('Quarter', None, None), # TODO: check parameter
        Parameter('Month', None, None), # TODO: check parameter
        Parameter('Day', None, None), # TODO: check parameter
        Parameter('Day of Week', None, None), # TODO: check parameter
        Parameter('Day of Year', None, None), # TODO: check parameter
        Parameter('Week of Year', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

time_field_extractor_legacy = Implementation(
    name='Time Field Extractor (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column containing time', None, None), # TODO: check parameter
        Parameter('Hour', None, None), # TODO: check parameter
        Parameter('Minute', None, None), # TODO: check parameter
        Parameter('Second', None, None), # TODO: check parameter
        Parameter('Millisecond', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

date_time_shift_legacy = Implementation(
    name='Date/Time Shift (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Use shift value from column', None, None), # TODO: check parameter
        Parameter('Use static shift value', None, None), # TODO: check parameter
        Parameter('Shift value', None, None), # TODO: check parameter
        Parameter('Select shift column', None, None), # TODO: check parameter
        Parameter('Select granularity of shift', None, None), # TODO: check parameter
        Parameter('Replace column', None, None), # TODO: check parameter
        Parameter('Appended column name', None, None), # TODO: check parameter
        Parameter('Use execution time', None, None), # TODO: check parameter
        Parameter('Use date/time column', None, None), # TODO: check parameter
        Parameter('Use fixed date', None, None), # TODO: check parameter
        Parameter('Select a date column', None, None), # TODO: check parameter
        Parameter('Fixed time', None, None), # TODO: check parameter
        Parameter('Use date', None, None), # TODO: check parameter
        Parameter('Use time', None, None), # TODO: check parameter
        Parameter('Use milliseconds', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

extract_time_window_legacy = Implementation(
    name='Extract Time Window (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Columns containing date/time', None, None), # TODO: check parameter
        Parameter('Starting point ', None, None), # TODO: check parameter
        Parameter('End point: ', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

mask_date_time_legacy = Implementation(
    name='Mask Date/Time (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column containing date/time', None, None), # TODO: check parameter
        Parameter('Replace selected column', None, None), # TODO: check parameter
        Parameter('Date', None, None), # TODO: check parameter
        Parameter('Time', None, None), # TODO: check parameter
        Parameter('Milliseconds', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

preset_date_time_legacy = Implementation(
    name='Preset Date/Time (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column containing date/time', None, None), # TODO: check parameter
        Parameter('Use date', None, None), # TODO: check parameter
        Parameter('Use time', None, None), # TODO: check parameter
        Parameter('Replace missing values', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

string_to_date_time_legacy = Implementation(
    name='String to Date/Time (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select column', None, None), # TODO: check parameter
        Parameter('Replace selected column', None, None), # TODO: check parameter
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('Date format', None, None), # TODO: check parameter
        Parameter('Abort execution', None, None), # TODO: check parameter
        Parameter('Maximum number of unresolved rows', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

time_difference_legacy = Implementation(
    name='Time Difference (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Use execution time', None, None), # TODO: check parameter
        Parameter('Use second column', None, None), # TODO: check parameter
        Parameter('Use fixed date', None, None), # TODO: check parameter
        Parameter('Use previous row', None, None), # TODO: check parameter
        Parameter('Select first date column', None, None), # TODO: check parameter
        Parameter('Select second date column', None, None), # TODO: check parameter
        Parameter('Select granularity of time difference', None, None), # TODO: check parameter
        Parameter('Rounding mode', None, None), # TODO: check parameter
        Parameter('Appended column name', None, None), # TODO: check parameter
        Parameter('Fixed time', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

time_generator_legacy = Implementation(
    name='Time Generator (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of rows', None, None), # TODO: check parameter
        Parameter('Use execution time as starting time', None, None), # TODO: check parameter
        Parameter('From', None, None), # TODO: check parameter
        Parameter('To', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

time_to_string_legacy = Implementation(
    name='Time to String (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column containing date/time', None, None), # TODO: check parameter
        Parameter('Replace selected column', None, None), # TODO: check parameter
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('Date format: ', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
