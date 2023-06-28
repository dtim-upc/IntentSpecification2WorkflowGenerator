from ontology_populator.implementations.core import *
from common import *

data_to_report = Implementation(
    name='Data to Report',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Use custom image scaling', None, None), # TODO: check parameter
        Parameter('Export Image As', None, None), # TODO: check parameter
        Parameter('Height', None, None), # TODO: check parameter
        Parameter('Width', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

image_to_report = Implementation(
    name='Image to Report',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Use custom image scaling', None, None), # TODO: check parameter
        Parameter('Export Image As', None, None), # TODO: check parameter
        Parameter('Height', None, None), # TODO: check parameter
        Parameter('Width', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.image.ImagePortObject'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
