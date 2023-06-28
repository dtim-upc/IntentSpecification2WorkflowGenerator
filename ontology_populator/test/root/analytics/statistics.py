from ontology_populator.implementations.core import *
from common import *

cronbach_alpha = Implementation(
    name='Cronbach Alpha',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

standardized_cronbach_alpha = Implementation(
    name='Standardized Cronbach Alpha',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.preproc.correlation.pmcc.PMCCPortObjectAndSpec'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

rank_correlation = Implementation(
    name='Rank Correlation',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.base.node.preproc.correlation.pmcc.PMCCPortObjectAndSpec'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

statistics = Implementation(
    name='Statistics',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

crosstab_local = Implementation(
    name='Crosstab (local)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Row variable', None, None), # TODO: check parameter
        Parameter('Column variable', None, None), # TODO: check parameter
        Parameter('Weight column', None, None), # TODO: check parameter
        Parameter('Enable hiliting', None, None), # TODO: check parameter
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

value_counter = Implementation(
    name='Value Counter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column', None, None), # TODO: check parameter
        Parameter('Enable hiliting', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

linear_correlation = Implementation(
    name='Linear Correlation',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.base.node.preproc.correlation.pmcc.PMCCPortObjectAndSpec'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

numeric_outliers = Implementation(
    name='Numeric Outliers',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.base.algorithms.outlier.NumericOutliersPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

numeric_outliers_apply = Implementation(
    name='Numeric Outliers (Apply)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.algorithms.outlier.NumericOutliersPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
