from ontology_populator.implementations.core import *
from common import *

scorer = Implementation(
    name='Scorer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('First column', None, None), # TODO: check parameter
        Parameter('Second column', None, None), # TODO: check parameter
        Parameter('Sorting strategy', None, None), # TODO: check parameter
        Parameter('Reverse order', None, None), # TODO: check parameter
        Parameter('Use name prefix', None, None), # TODO: check parameter
        Parameter('Missing Values', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

numeric_scorer = Implementation(
    name='Numeric Scorer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Reference column', None, None), # TODO: check parameter
        Parameter('Predicted column', None, None), # TODO: check parameter
        Parameter('Change column name', None, None), # TODO: check parameter
        Parameter('Output column name', None, None), # TODO: check parameter
        Parameter('Prefix of flow variables', None, None), # TODO: check parameter
        Parameter('Output scores as flow variables', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

entropy_scorer = Implementation(
    name='Entropy Scorer',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Reference column', None, None), # TODO: check parameter
        Parameter('Clustering column', None, None), # TODO: check parameter
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

roc_curve_local = Implementation(
    name='ROC Curve (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Class column', None, None), # TODO: check parameter
        Parameter('Positive class value', None, None), # TODO: check parameter
        Parameter('Limit data points for each curve to', None, None), # TODO: check parameter
        Parameter('Columns containing the positive class probabilities', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

enrichment_plotter_local = Implementation(
    name='Enrichment Plotter (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Plot sum of hit values', None, None), # TODO: check parameter
        Parameter('Plot hits', None, None), # TODO: check parameter
        Parameter('Plot discovered clusters', None, None), # TODO: check parameter
        Parameter('Fraction sizes (in %)', None, None), # TODO: check parameter
        Parameter('Sort column', None, None), # TODO: check parameter
        Parameter('Activity column', None, None), # TODO: check parameter
        Parameter('Sort descending', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

silhouette_coefficient = Implementation(
    name='Silhouette Coefficient',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Data Column Selection', None, None), # TODO: check parameter
        Parameter('Clustering Column Selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
