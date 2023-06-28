from ontology_populator.implementations.core import *
from common import *

random_forest_distance = Implementation(
    name='Random Forest Distance',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.treeensemble2.model.TreeEnsembleModelPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.distance.DistanceMeasurePortObject'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

tree_ensemble_model_extract = Implementation(
    name='Tree Ensemble Model Extract',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Target Column', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.treeensemble2.model.TreeEnsembleModelPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

tree_ensemble_statistics = Implementation(
    name='Tree Ensemble Statistics',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.treeensemble2.model.TreeEnsembleModelPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
