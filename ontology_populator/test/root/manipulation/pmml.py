from ontology_populator.implementations.core import *
from common import *

column_filter_pmml = Implementation(
    name='Column Filter (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

denormalizer_pmml = Implementation(
    name='Denormalizer (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

many_to_one_pmml = Implementation(
    name='Many to One (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Columns', None, None), # TODO: check parameter
        Parameter('Condensed column name', None, None), # TODO: check parameter
        Parameter('Include method', None, None), # TODO: check parameter
        Parameter('Include pattern', None, None), # TODO: check parameter
        Parameter('Keep original columns', None, None), # TODO: check parameter
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

normalizer_pmml = Implementation(
    name='Normalizer (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Min-max normalization', None, None), # TODO: check parameter
        Parameter('Z-score normalization', None, None), # TODO: check parameter
        Parameter('Normalization by decimal scaling', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

number_to_string_pmml = Implementation(
    name='Number To String (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Selection', None, None), # TODO: check parameter
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

normalizer_apply_pmml = Implementation(
    name='Normalizer Apply (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

numeric_binner_pmml = Implementation(
    name='Numeric Binner (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select Column: ', None, None), # TODO: check parameter
        Parameter('Append new column: ', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

one_to_many_pmml = Implementation(
    name='One to Many (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Columns', None, None), # TODO: check parameter
        Parameter('Remove included columns from output', None, None), # TODO: check parameter
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

ruleset_editor = Implementation(
    name='Ruleset Editor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column List', None, None), # TODO: check parameter
        Parameter('Category', None, None), # TODO: check parameter
        Parameter('Function', None, None), # TODO: check parameter
        Parameter('Description', None, None), # TODO: check parameter
        Parameter('Expression', None, None), # TODO: check parameter
        Parameter('Appended Column', None, None), # TODO: check parameter
        Parameter('Replace Column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

ruleset_predictor = Implementation(
    name='Ruleset Predictor',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Append Column', None, None), # TODO: check parameter
        Parameter('Replace Column', None, None), # TODO: check parameter
        Parameter('Compute confidence?', None, None), # TODO: check parameter
        Parameter('Confidence column', None, None), # TODO: check parameter
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

ruleset_to_table = Implementation(
    name='Ruleset to Table',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Split rules to condition and outcome columns', None, None), # TODO: check parameter
        Parameter('Add confidence and weight columns', None, None), # TODO: check parameter
        Parameter('Add Record count and Number of correct statistics columns', None, None), # TODO: check parameter
        Parameter('Use additional parentheses to document precedence rules', None, None), # TODO: check parameter
        Parameter('Provide score distibution record count in table with column name prefix', None, None), # TODO: check parameter
        Parameter('Provide score distibution probability in table with column name prefix', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)

string_to_number_pmml = Implementation(
    name='String To Number (PMML)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Type', None, None), # TODO: check parameter
        Parameter('Decimal Separator', None, None), # TODO: check parameter
        Parameter('Thousands Separator', None, None), # TODO: check parameter
        Parameter('Column Selection', None, None), # TODO: check parameter
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

xml_to_pmml = Implementation(
    name='XML To PMML',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('XML Column', None, None), # TODO: check parameter
        Parameter('Replace existing column', None, None), # TODO: check parameter
        Parameter('New PMML Column', None, None), # TODO: check parameter
        Parameter('Fail on invalid PMML', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

cell_to_pmml = Implementation(
    name='Cell To PMML',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select the model column', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    implementation_type=do.LearnerImplementation # TODO: check implementation type
)

pmml_to_cell = Implementation(
    name='PMML To Cell',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Row Identifier', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.pmml.PMMLPortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.ApplierImplementation # TODO: check implementation type
)
