from ontology_populator.implementations.core import *
from common import *

column_filter_legacy = Implementation(
    name='Column Filter (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Hide in Dialog', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Default Values', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

range_slider_filter_definition_legacy = Implementation(
    name='Range Slider Filter Definition (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

value_filter_legacy = Implementation(
    name='Value Filter (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Hide in Dialog', None, None), # TODO: check parameter
        Parameter('Variable Name', None, None), # TODO: check parameter
        Parameter('Parameter Name', None, None), # TODO: check parameter
        Parameter('Selection Type', None, None), # TODO: check parameter
        Parameter('Lock Column', None, None), # TODO: check parameter
        Parameter('Default Column', None, None), # TODO: check parameter
        Parameter('Default Values', None, None), # TODO: check parameter
        Parameter('Limit number of visible options', None, None), # TODO: check parameter
        Parameter('Number of visible options', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

value_filter_definition_legacy = Implementation(
    name='Value Filter Definition (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.viewproperty.FilterDefinitionHandlerPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
