from ontology_populator.implementations.core import *
from common import *

interactive_range_slider_filter_widget = Implementation(
    name='Interactive Range Slider Filter Widget',
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

interactive_value_filter_widget = Implementation(
    name='Interactive Value Filter Widget',
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
