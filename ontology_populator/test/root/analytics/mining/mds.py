from ontology_populator.implementations.core import *
from common import *

mds = Implementation(
    name='MDS',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of rows to use', None, None), # TODO: check parameter
        Parameter('Output dimension', None, None), # TODO: check parameter
        Parameter('Epochs', None, None), # TODO: check parameter
        Parameter('Learn rate', None, None), # TODO: check parameter
        Parameter('Random seed', None, None), # TODO: check parameter
        Parameter('Distance metric', None, None), # TODO: check parameter
        Parameter('Input data', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

mds_distmatrix = Implementation(
    name='MDS (DistMatrix)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of rows to use', None, None), # TODO: check parameter
        Parameter('Output dimension', None, None), # TODO: check parameter
        Parameter('Epochs', None, None), # TODO: check parameter
        Parameter('Learn rate', None, None), # TODO: check parameter
        Parameter('Random seed', None, None), # TODO: check parameter
        Parameter('Distance matrix column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

mds_projection = Implementation(
    name='MDS Projection',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of rows to use', None, None), # TODO: check parameter
        Parameter('Output dimension', None, None), # TODO: check parameter
        Parameter('Epochs', None, None), # TODO: check parameter
        Parameter('Learn rate', None, None), # TODO: check parameter
        Parameter('Random seed', None, None), # TODO: check parameter
        Parameter('Distance metric', None, None), # TODO: check parameter
        Parameter('Project only', None, None), # TODO: check parameter
        Parameter('Input data', None, None), # TODO: check parameter
        Parameter('Fixed data', None, None), # TODO: check parameter
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

mds_projection_distmatrix = Implementation(
    name='MDS Projection (DistMatrix)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of rows to use', None, None), # TODO: check parameter
        Parameter('Project only', None, None), # TODO: check parameter
        Parameter('Epochs', None, None), # TODO: check parameter
        Parameter('Learn rate', None, None), # TODO: check parameter
        Parameter('Random seed', None, None), # TODO: check parameter
        Parameter('Output dimension', None, None), # TODO: check parameter
        Parameter('Distance matrix column of data to project', None, None), # TODO: check parameter
        Parameter('MDS columns', None, None), # TODO: check parameter
        Parameter('Distance matrix column of fixed data', None, None), # TODO: check parameter
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
