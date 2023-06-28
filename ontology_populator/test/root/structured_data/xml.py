from ontology_populator.implementations.core import *
from common import *

string_to_xml = Implementation(
    name='String To XML',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

xpath = Implementation(
    name='XPath',
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

xslt = Implementation(
    name='XSLT',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('XML column', None, None), # TODO: check parameter
        Parameter('Remove source column', None, None), # TODO: check parameter
        Parameter('Stylesheet column', None, None), # TODO: check parameter
        Parameter('Use first stylesheet only', None, None), # TODO: check parameter
        Parameter('Output is XML', None, None), # TODO: check parameter
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

column_to_xml = Implementation(
    name='Column To XML',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('Content column', None, None), # TODO: check parameter
        Parameter('Element name', None, None), # TODO: check parameter
        Parameter('Data bound attributes', None, None), # TODO: check parameter
        Parameter('Custom attributes', None, None), # TODO: check parameter
        Parameter('Remove source columns', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

xml_column_combiner = Implementation(
    name='XML Column Combiner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('Exclude / Include', None, None), # TODO: check parameter
        Parameter('Remove source columns', None, None), # TODO: check parameter
        Parameter('Element name', None, None), # TODO: check parameter
        Parameter('Data bound attributes', None, None), # TODO: check parameter
        Parameter('Custom attributes', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

xml_row_combiner = Implementation(
    name='XML Row Combiner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('XML column', None, None), # TODO: check parameter
        Parameter('New column name', None, None), # TODO: check parameter
        Parameter('Element name', None, None), # TODO: check parameter
        Parameter('Custom attributes', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

xml_row_combine_and_write = Implementation(
    name='XML Row Combine and Write',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('XML column', None, None), # TODO: check parameter
        Parameter('Selected file', None, None), # TODO: check parameter
        Parameter('Overwrite existing files', None, None), # TODO: check parameter
        Parameter('Root element', None, None), # TODO: check parameter
        Parameter('Attributes of the root element', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

xml_reader = Implementation(
    name='XML Reader',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

xml_writer = Implementation(
    name='XML Writer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Write to', None, None), # TODO: check parameter
        Parameter('Folder', None, None), # TODO: check parameter
        Parameter('Create missing folders', None, None), # TODO: check parameter
        Parameter('If exists', None, None), # TODO: check parameter
        Parameter('XML', None, None), # TODO: check parameter
        Parameter('File names', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
