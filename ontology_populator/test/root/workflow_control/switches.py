from ontology_populator.implementations.core import *
from common import *

if_switch = Implementation(
    name='IF Switch',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select active port', None, None), # TODO: check parameter
        Parameter('Activate all outputs during configuration step', None, None), # TODO: check parameter
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

end_if = Implementation(
    name='End IF',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Skip Rows', None, None), # TODO: check parameter
        Parameter('Append Suffix', None, None), # TODO: check parameter
        Parameter('Enable hiliting', None, None), # TODO: check parameter
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

case_switch_start = Implementation(
    name='CASE Switch Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Select active port', None, None), # TODO: check parameter
        Parameter('Activate all outputs during configuration step', None, None), # TODO: check parameter
    ],
    input=[
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

case_switch_end = Implementation(
    name='CASE Switch End',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
    ],
    output=[
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

empty_table_switch = Implementation(
    name='Empty Table Switch',
    algorithm=None, # TODO: check algorithm
    parameters=[
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

java_if_table = Implementation(
    name='Java IF (Table)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Method Body', None, None), # TODO: check parameter
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
