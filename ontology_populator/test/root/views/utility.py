from ontology_populator.implementations.core import *
from common import *

css_editor = Implementation(
    name='CSS Editor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Prepend existing stylesheet', None, None), # TODO: check parameter
        Parameter('Append new variable', None, None), # TODO: check parameter
        Parameter('Replace existing variable', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

image_to_table = Implementation(
    name='Image To Table',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Row Identifier', None, None), # TODO: check parameter
        Parameter('Column Name', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.image.ImagePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

table_to_image = Implementation(
    name='Table To Image',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Image column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.image.ImagePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

renderer_to_image = Implementation(
    name='Renderer to Image',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column', None, None), # TODO: check parameter
        Parameter('Renderer', None, None), # TODO: check parameter
        Parameter('Image type', None, None), # TODO: check parameter
        Parameter('Image size', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

string_to_svg = Implementation(
    name='String To SVG',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Input Column', None, None), # TODO: check parameter
        Parameter('Replace/Append Column', None, None), # TODO: check parameter
        Parameter('Fail on invalid input cell', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
