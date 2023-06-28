from ontology_populator.implementations.core import *
from common import *

distance_matrix_reader = Implementation(
    name='Distance Matrix Reader',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('URL', None, None), # TODO: check parameter
        Parameter('Separator Char', None, None), # TODO: check parameter
        Parameter('Read Row Header', None, None), # TODO: check parameter
        Parameter('Read Column Header', None, None), # TODO: check parameter
        Parameter('File contains full matrix', None, None), # TODO: check parameter
        Parameter('Matrix is symmetric', None, None), # TODO: check parameter
        Parameter('File contains triangular matrix', None, None), # TODO: check parameter
        Parameter('Contains Diagonal', None, None), # TODO: check parameter
        Parameter('Apply linear transformation', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

distance_matrix_writer = Implementation(
    name='Distance Matrix Writer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Output File', None, None), # TODO: check parameter
        Parameter('Distance Matrix Column', None, None), # TODO: check parameter
        Parameter('Write Column/Row Header', None, None), # TODO: check parameter
        Parameter('Separator Char', None, None), # TODO: check parameter
        Parameter('Overwrite OK', None, None), # TODO: check parameter
        Parameter('Writer Lower Triangular Matrix', None, None), # TODO: check parameter
        Parameter('Writer Upper Triangular Matrix', None, None), # TODO: check parameter
        Parameter('Writer Full Matrix', None, None), # TODO: check parameter
        Parameter('Writer diagonal values', None, None), # TODO: check parameter
        Parameter('Chunk Size', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

distance_matrix_calculate = Implementation(
    name='Distance Matrix Calculate',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Distance Function', None, None), # TODO: check parameter
        Parameter('Column Selection', None, None), # TODO: check parameter
        Parameter('Appended Column Name', None, None), # TODO: check parameter
        Parameter('Chunk Size', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

distance_matrix_pair_extractor = Implementation(
    name='Distance Matrix Pair Extractor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Name column', None, None), # TODO: check parameter
        Parameter('Distance vector column', None, None), # TODO: check parameter
        Parameter('Comparator', None, None), # TODO: check parameter
        Parameter('Threshold', None, None), # TODO: check parameter
        Parameter('Cache distances', None, None), # TODO: check parameter
        Parameter('Add distance column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

similarity_search = Implementation(
    name='Similarity Search',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Distance function', None, None), # TODO: check parameter
        Parameter('Column Selection', None, None), # TODO: check parameter
        Parameter('Coefficient Type', None, None), # TODO: check parameter
        Parameter('Neighbor Selection', None, None), # TODO: check parameter
        Parameter('Range Filtering', None, None), # TODO: check parameter
        Parameter('Output column name prefix', None, None), # TODO: check parameter
        Parameter('Representative Column', None, None), # TODO: check parameter
        Parameter('RowID Suffix Separator', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
