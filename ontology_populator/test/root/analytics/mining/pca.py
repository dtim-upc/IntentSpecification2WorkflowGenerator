from ontology_populator.implementations.core import *
from common import *

pca = Implementation(
    name='PCA',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Target dimensions', None, None), # TODO: check parameter
        Parameter('Columns', None, None), # TODO: check parameter
        Parameter('Remove original data columns', None, None), # TODO: check parameter
        Parameter('Fail if missing values are encountered', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

pca_compute = Implementation(
    name='PCA Compute',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Columns', None, None), # TODO: check parameter
        Parameter('Fail if missing values are encountered', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.base.node.mine.transformation.port.TransformationPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

pca_apply = Implementation(
    name='PCA Apply',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Target dimensions', None, None), # TODO: check parameter
        Parameter('Remove original data columns', None, None), # TODO: check parameter
        Parameter('Fail if missing values are encountered', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.transformation.port.TransformationPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

pca_inversion = Implementation(
    name='PCA Inversion',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Columns', None, None), # TODO: check parameter
        Parameter('Remove selected columns', None, None), # TODO: check parameter
        Parameter('Fail if missing values are encountered', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.transformation.port.TransformationPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
