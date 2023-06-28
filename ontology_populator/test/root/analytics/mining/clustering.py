from ontology_populator.implementations.core import *
from common import *

cluster_assigner = Implementation(
    name='Cluster Assigner',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

dbscan = Implementation(
    name='DBSCAN',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Epsilon', None, None), # TODO: check parameter
        Parameter('Minimum points', None, None), # TODO: check parameter
        Parameter('Load data in memory', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

fuzzy_c-means = Implementation(
    name='Fuzzy c-Means',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of clusters', None, None), # TODO: check parameter
        Parameter('Maximum number of iterations', None, None), # TODO: check parameter
        Parameter('Fuzzifier', None, None), # TODO: check parameter
        Parameter('Use seed for random initialization', None, None), # TODO: check parameter
        Parameter('Induce noise cluster', None, None), # TODO: check parameter
        Parameter('Set delta', None, None), # TODO: check parameter
        Parameter('Set delta automatically, specify lambda', None, None), # TODO: check parameter
        Parameter('Perform the clustering in memory', None, None), # TODO: check parameter
        Parameter('Compute cluster quality measures', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

hierarchical_clustering = Implementation(
    name='Hierarchical Clustering',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number output cluster', None, None), # TODO: check parameter
        Parameter('Distance function', None, None), # TODO: check parameter
        Parameter('Linkage type', None, None), # TODO: check parameter
        Parameter('Distance cache', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

sota_learner = Implementation(
    name='SOTA Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Winner learningrate', None, None), # TODO: check parameter
        Parameter('Sister learningrate', None, None), # TODO: check parameter
        Parameter('Ancestor learningrate', None, None), # TODO: check parameter
        Parameter('Minimal variability', None, None), # TODO: check parameter
        Parameter('Minimal resource', None, None), # TODO: check parameter
        Parameter('Minimal error', None, None), # TODO: check parameter
        Parameter('Use variability', None, None), # TODO: check parameter
        Parameter('Distance metric', None, None), # TODO: check parameter
        Parameter('Use hierarchical fuzzy data', None, None), # TODO: check parameter
        Parameter('Hierarchical level', None, None), # TODO: check parameter
        Parameter('Use class column', None, None), # TODO: check parameter
        Parameter('Class column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.base.node.mine.sota.SotaPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

sota_predictor = Implementation(
    name='SOTA Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Prediction Column', None, None), # TODO: check parameter
        Parameter('Append columns with normalized class distribution', None, None), # TODO: check parameter
        Parameter('Suffix for probability columns', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.sota.SotaPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

k-means = Implementation(
    name='k-Means',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of clusters', None, None), # TODO: check parameter
        Parameter('Centroid initialization', None, None), # TODO: check parameter
        Parameter('Max number of iterations', None, None), # TODO: check parameter
        Parameter('Numeric Column Selection', None, None), # TODO: check parameter
        Parameter('Enable Hilite Mapping', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

k-medoids = Implementation(
    name='k-Medoids',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Partition Count (k)', None, None), # TODO: check parameter
        Parameter('Distance Column', None, None), # TODO: check parameter
        Parameter('Chunk Size', None, None), # TODO: check parameter
        Parameter('Constraint no. iterations', None, None), # TODO: check parameter
        Parameter('Use static seed', None, None), # TODO: check parameter
        Parameter('Output relative distances to medoids', None, None), # TODO: check parameter
        Parameter('Choke on asymmetric distances', None, None), # TODO: check parameter
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

hierarchical_clustering_distmatrix = Implementation(
    name='Hierarchical Clustering (DistMatrix)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Distance matrix column', None, None), # TODO: check parameter
        Parameter('Linkage type', None, None), # TODO: check parameter
        Parameter('Ignore missing values', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.base.node.mine.cluster.hierarchical.ClusterTreeModel'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

hierarchical_cluster_view = Implementation(
    name='Hierarchical Cluster View',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.cluster.hierarchical.ClusterTreeModel'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

hierarchical_cluster_assigner_local = Implementation(
    name='Hierarchical Cluster Assigner (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Assign clusters based on', None, None), # TODO: check parameter
        Parameter('Number of clusters', None, None), # TODO: check parameter
        Parameter('Distance threshold', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.cluster.hierarchical.ClusterTreeModel'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
