from ontology_populator.implementations.core import *
from common import *

file_download_legacy = Implementation(
    name='File Download (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Link Title', None, None), # TODO: check parameter
        Parameter('Output resource name', None, None), # TODO: check parameter
        Parameter('File Path Variable', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

image_output_legacy = Implementation(
    name='Image Output (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Maximum Width', None, None), # TODO: check parameter
        Parameter('Maximum Height', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.image.ImagePortObject'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

text_output_legacy = Implementation(
    name='Text Output (legacy)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Label', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Text format', None, None), # TODO: check parameter
        Parameter('Text', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
