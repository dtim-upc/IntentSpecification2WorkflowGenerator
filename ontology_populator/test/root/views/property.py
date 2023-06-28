from ontology_populator.implementations.core import *
from common import *

color_manager = Implementation(
    name='Color Manager',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column(s): ', None, None), # TODO: check parameter
        Parameter('Nominal: ', None, None), # TODO: check parameter
        Parameter('Range: ', None, None), # TODO: check parameter
        Parameter('Alpha: ', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.viewproperty.ColorHandlerPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

size_manager = Implementation(
    name='Size Manager',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column selection', None, None), # TODO: check parameter
        Parameter('Scaling factor', None, None), # TODO: check parameter
        Parameter('Mapping method', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.viewproperty.SizeHandlerPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

shape_manager = Implementation(
    name='Shape Manager',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select nominal column: ', None, None), # TODO: check parameter
        Parameter('Shape Mapping: ', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.viewproperty.ShapeHandlerPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

color_appender = Implementation(
    name='Color Appender',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Append colors to: ', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.ColorHandlerPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

size_appender = Implementation(
    name='Size Appender',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Append sizes to: ', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.SizeHandlerPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

shape_appender = Implementation(
    name='Shape Appender',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Append shapes to: ', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.ShapeHandlerPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

extract_color = Implementation(
    name='Extract Color',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.viewproperty.ColorHandlerPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
