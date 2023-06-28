from ontology_populator.implementations.core import *
from common import *

breakpoint = Implementation(
    name='Breakpoint',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Breakpoint Enabled', None, None), # TODO: check parameter
        Parameter('Breakpoint active for', None, None), # TODO: check parameter
        Parameter('Custom message', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

counting_loop_start = Implementation(
    name='Counting Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Number of loops', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

chunk_loop_start = Implementation(
    name='Chunk Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Rows per chunk', None, None), # TODO: check parameter
        Parameter('No. of chunks', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

column_list_loop_start = Implementation(
    name='Column List Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column Filter', None, None), # TODO: check parameter
        Parameter('If include column list is empty', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

generic_loop_start = Implementation(
    name='Generic Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

table_row_to_variable_loop_start = Implementation(
    name='Table Row To Variable Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Missing value handling', None, None), # TODO: check parameter
        Parameter('Defaults', None, None), # TODO: check parameter
        Parameter('Column selection', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

loop_end = Implementation(
    name='Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Row ID policy', None, None), # TODO: check parameter
        Parameter('Add iteration column', None, None), # TODO: check parameter
        Parameter('Propagate modified loop variables', None, None), # TODO: check parameter
        Parameter('Ignore empty input tables', None, None), # TODO: check parameter
        Parameter('Allow variable column types', None, None), # TODO: check parameter
        Parameter('Allow changing table specifications', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

variable_condition_loop_end = Implementation(
    name='Variable Condition Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Available variables', None, None), # TODO: check parameter
        Parameter('Collect rows from last iteration', None, None), # TODO: check parameter
        Parameter('Collect rows from last iteration only', None, None), # TODO: check parameter
        Parameter('Add iteration column', None, None), # TODO: check parameter
        Parameter('Propagate modified loop variables', None, None), # TODO: check parameter
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

variable_loop_end = Implementation(
    name='Variable Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Variable selection', None, None), # TODO: check parameter
        Parameter('Propagate modified loop variables', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

group_loop_start = Implementation(
    name='Group Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column selection', None, None), # TODO: check parameter
        Parameter('Input is already sorted by group column(s)', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

interval_loop_start = Implementation(
    name='Interval Loop Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('From', None, None), # TODO: check parameter
        Parameter('To', None, None), # TODO: check parameter
        Parameter('Step', None, None), # TODO: check parameter
        Parameter('Loop variable is', None, None), # TODO: check parameter
        Parameter('Variable prefix', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

loop_end_column_append = Implementation(
    name='Loop End (Column Append)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Loop has same row IDs in each iteration', None, None), # TODO: check parameter
        Parameter('Propagate modified loop variables', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

recursive_loop_end = Implementation(
    name='Recursive Loop End',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Maximal number of iterations', None, None), # TODO: check parameter
        Parameter('Minimal number of rows', None, None), # TODO: check parameter
        Parameter('End loop with variable', None, None), # TODO: check parameter
        Parameter('Collect data from last iteration only', None, None), # TODO: check parameter
        Parameter('Add iteration column', None, None), # TODO: check parameter
        Parameter('Propagate modified loop variables', None, None), # TODO: check parameter
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

recursive_loop_start = Implementation(
    name='Recursive Loop Start',
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
