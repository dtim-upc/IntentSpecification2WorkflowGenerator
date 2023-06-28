from ontology_populator.implementations.core import *
from common import *

numeric_distances = Implementation(
    name='Numeric Distances',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Selection', None, None), # TODO: check parameter
        Parameter('Distance Selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

string_distances = Implementation(
    name='String Distances',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Selection', None, None), # TODO: check parameter
        Parameter('Distance Selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

bit_vector_distances = Implementation(
    name='Bit Vector Distances',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Selection', None, None), # TODO: check parameter
        Parameter('Distance Selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

byte_vector_distances = Implementation(
    name='Byte Vector Distances',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Selection', None, None), # TODO: check parameter
        Parameter('Distance Selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

mahalanobis_distance = Implementation(
    name='Mahalanobis Distance',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

matrix_distance = Implementation(
    name='Matrix Distance',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

aggregated_distance = Implementation(
    name='Aggregated Distance',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Distances', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

java_distance = Implementation(
    name='Java Distance',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column List', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
