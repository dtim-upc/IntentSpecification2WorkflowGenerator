from ontology_populator.implementations.core import *
from common import *

duplicate_row_filter = Implementation(
    name='Duplicate Row Filter',
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

filter_apply = Implementation(
    name='Filter Apply',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

filter_apply_row_splitter = Implementation(
    name='Filter Apply Row Splitter',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

filter_definition_merger = Implementation(
    name='Filter Definition Merger',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

hilite_row_splitter = Implementation(
    name='HiLite Row Splitter',
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

nominal_value_row_filter = Implementation(
    name='Nominal Value Row Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select column', None, None), # TODO: check parameter
        Parameter('Nominal value selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

nominal_value_row_splitter = Implementation(
    name='Nominal Value Row Splitter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select column', None, None), # TODO: check parameter
        Parameter('Nominal value selection', None, None), # TODO: check parameter
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

numeric_row_splitter = Implementation(
    name='Numeric Row Splitter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column selection: ', None, None), # TODO: check parameter
        Parameter('Lower bound: ', None, None), # TODO: check parameter
        Parameter('Upper bound: ', None, None), # TODO: check parameter
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

reference_row_filter = Implementation(
    name='Reference Row Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Data table column', None, None), # TODO: check parameter
        Parameter('Reference table column', None, None), # TODO: check parameter
        Parameter('In-/Exclude rows from reference table', None, None), # TODO: check parameter
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

reference_row_splitter = Implementation(
    name='Reference Row Splitter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Data table column', None, None), # TODO: check parameter
        Parameter('Reference table column', None, None), # TODO: check parameter
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

row_filter = Implementation(
    name='Row Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('In- or exclude rows by criteria', None, None), # TODO: check parameter
        Parameter('Column value matching', None, None), # TODO: check parameter
        Parameter('Row number range', None, None), # TODO: check parameter
        Parameter('Row ID pattern', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

row_splitter = Implementation(
    name='Row Splitter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('In- or exclude rows by criteria', None, None), # TODO: check parameter
        Parameter('Column value matching', None, None), # TODO: check parameter
        Parameter('Row number range', None, None), # TODO: check parameter
        Parameter('Row ID pattern', None, None), # TODO: check parameter
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

rule-based_row_filter = Implementation(
    name='Rule-based Row Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column List', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Category', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
        Parameter('Include TRUE matches', None, None), # TODO: check parameter
        Parameter('Exclude TRUE matches', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

rule-based_row_filter_dictionary = Implementation(
    name='Rule-based Row Filter (Dictionary)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Rules column', None, None), # TODO: check parameter
        Parameter('=>', None, None), # TODO: check parameter
        Parameter('Treat values starting with $ as references', None, None), # TODO: check parameter
        Parameter('Include TRUE matches', None, None), # TODO: check parameter
        Parameter('Exclude TRUE matches', None, None), # TODO: check parameter
        Parameter('Errors', None, None), # TODO: check parameter
        Parameter('Warnings', None, None), # TODO: check parameter
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

rule-based_row_splitter = Implementation(
    name='Rule-based Row Splitter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column List', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Category', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
        Parameter('TRUE matches go to', None, None), # TODO: check parameter
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

rule-based_row_splitter_dictionary = Implementation(
    name='Rule-based Row Splitter (Dictionary)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Rules column', None, None), # TODO: check parameter
        Parameter('=>', None, None), # TODO: check parameter
        Parameter('Treat values starting with $ as references', None, None), # TODO: check parameter
        Parameter('TRUE matches go to', None, None), # TODO: check parameter
        Parameter('Errors', None, None), # TODO: check parameter
        Parameter('Warnings', None, None), # TODO: check parameter
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
