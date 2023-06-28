from ontology_populator.implementations.core import *
from common import *

pnn_learner_dda = Implementation(
    name='PNN Learner (DDA)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Missing Values', None, None), # TODO: check parameter
        Parameter('Advanced', None, None), # TODO: check parameter
        Parameter('Maximum no. Epochs', None, None), # TODO: check parameter
        Parameter('Target Columns', None, None), # TODO: check parameter
        Parameter('PNN', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.base.node.mine.bfn.radial.RadialBasisFunctionPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

pnn_predictor = Implementation(
    name='PNN Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Don't Know Class', None, None), # TODO: check parameter
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Prediction Column', None, None), # TODO: check parameter
        Parameter('Append columns with normalized class distribution', None, None), # TODO: check parameter
        Parameter('Suffix for probability columns', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.bfn.radial.RadialBasisFunctionPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
