from ontology_populator.implementations.core import *
from common import *

java_snippet = Implementation(
    name='Java Snippet',
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

java_snippet_simple = Implementation(
    name='Java Snippet (simple)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column List', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Global Variable Declaration', None, None), # TODO: check parameter
        Parameter('Method Body', None, None), # TODO: check parameter
        Parameter('Insert Missing As Null', None, None), # TODO: check parameter
        Parameter('Compile on close', None, None), # TODO: check parameter
        Parameter('Return type', None, None), # TODO: check parameter
        Parameter('Array Return', None, None), # TODO: check parameter
        Parameter('Replace/Append', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

java_snippet_row_filter = Implementation(
    name='Java Snippet Row Filter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column List', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Global Variable Declaration', None, None), # TODO: check parameter
        Parameter('Method Body', None, None), # TODO: check parameter
        Parameter('Insert Missing As Null', None, None), # TODO: check parameter
        Parameter('Compile on close', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

java_snippet_row_splitter = Implementation(
    name='Java Snippet Row Splitter',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Column List', None, None), # TODO: check parameter
        Parameter('Flow Variable List', None, None), # TODO: check parameter
        Parameter('Global Variable Declaration', None, None), # TODO: check parameter
        Parameter('Method Body', None, None), # TODO: check parameter
        Parameter('Insert Missing As Null', None, None), # TODO: check parameter
        Parameter('Compile on close', None, None), # TODO: check parameter
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
