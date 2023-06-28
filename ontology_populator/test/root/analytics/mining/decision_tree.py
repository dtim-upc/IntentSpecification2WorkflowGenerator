from ontology_populator.implementations.core import *
from common import *

decision_tree_learner = Implementation(
    name='Decision Tree Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Class column', None, None), # TODO: check parameter
        Parameter('Quality measure', None, None), # TODO: check parameter
        Parameter('Pruning method', None, None), # TODO: check parameter
        Parameter('Reduced Error Pruning', None, None), # TODO: check parameter
        Parameter('Min number records per node', None, None), # TODO: check parameter
        Parameter('Number records to store for view', None, None), # TODO: check parameter
        Parameter('Average split point', None, None), # TODO: check parameter
        Parameter('Number threads', None, None), # TODO: check parameter
        Parameter('Skip nominal columns without domain information', None, None), # TODO: check parameter
        Parameter('Force root split column', None, None), # TODO: check parameter
        Parameter('Binary nominal splits', None, None), # TODO: check parameter
        Parameter('Max #nominal', None, None), # TODO: check parameter
        Parameter('Filter invalid attribute values in child nodes', None, None), # TODO: check parameter
        Parameter('No true child strategy', None, None), # TODO: check parameter
        Parameter('Missing value strategy', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

decision_tree_predictor = Implementation(
    name='Decision Tree Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of patterns for HiLite', None, None), # TODO: check parameter
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Prediction Column', None, None), # TODO: check parameter
        Parameter('Append columns with normalized class distribution', None, None), # TODO: check parameter
        Parameter('Suffix for probability columns', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

decision_tree_to_image = Implementation(
    name='Decision Tree To Image',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Width (in Pixel)', None, None), # TODO: check parameter
        Parameter('Collapse Table', None, None), # TODO: check parameter
        Parameter('Tree Scaling', None, None), # TODO: check parameter
        Parameter('Zoom', None, None), # TODO: check parameter
        Parameter('Branch Display', None, None), # TODO: check parameter
        Parameter('Node Display', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.image.ImagePortObject'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

decision_tree_to_ruleset = Implementation(
    name='Decision Tree to Ruleset',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Split rules to condition and outcome columns', None, None), # TODO: check parameter
        Parameter('Add confidence and weight columns', None, None), # TODO: check parameter
        Parameter('Add Record count and Number of correct statistics columns', None, None), # TODO: check parameter
        Parameter('Use additional parentheses to document precedence rules', None, None), # TODO: check parameter
        Parameter('Provide score distibution record count in PMML', None, None), # TODO: check parameter
        Parameter('Provide score distibution record count in table with column name prefix', None, None), # TODO: check parameter
        Parameter('Provide score distibution probability in PMML', None, None), # TODO: check parameter
        Parameter('Provide score distibution probability in table with column name prefix', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

pmml_simple_regression_tree_predictor = Implementation(
    name='PMML Simple Regression Tree Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Prediction column name', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

simple_regression_tree_learner = Implementation(
    name='Simple Regression Tree Learner',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.base.node.mine.treeensemble2.model.RegressionTreeModelPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

simple_regression_tree_predictor = Implementation(
    name='Simple Regression Tree Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Change prediction column name', None, None), # TODO: check parameter
        Parameter('Prediction column name', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.treeensemble2.model.RegressionTreeModelPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

simple_regression_tree_to_pmml = Implementation(
    name='Simple Regression Tree to PMML',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.base.node.mine.treeensemble2.model.RegressionTreeModelPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
