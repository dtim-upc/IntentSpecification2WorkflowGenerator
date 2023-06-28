from ontology_populator.implementations.core import *
from common import *

k_nearest_neighbor = Implementation(
    name='K Nearest Neighbor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column with class labels', None, None), # TODO: check parameter
        Parameter('Number of neighbours to consider (k)', None, None), # TODO: check parameter
        Parameter('Weight neighbours by distance', None, None), # TODO: check parameter
        Parameter('Output class probabilities', None, None), # TODO: check parameter
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

k_nearest_neighbor_distance_function = Implementation(
    name='K Nearest Neighbor (Distance Function)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column with class labels', None, None), # TODO: check parameter
        Parameter('Number of neighbours to consider (k)', None, None), # TODO: check parameter
        Parameter('Weight neighbours by distance', None, None), # TODO: check parameter
        Parameter('Output class probabilities', None, None), # TODO: check parameter
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
