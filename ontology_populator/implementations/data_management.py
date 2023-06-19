from .implementation import *
from common import *

train_test_split = Implementation(
    name='Train-Test Split',
    algorithm=da.TrainTestSplit,
    parameters=[
        Parameter('Test Size', XSD.float, 0.2),
        Parameter('Random Sample', XSD.boolean, True),
        Parameter('Random State', XSD.integer, None),
    ],
    input=[
        ds.TabularDataset,
    ],
    output=[
        ds.TrainDataset,
        ds.TestDataset,
    ],
    transformations=[
        CopyTransformation(1, 1),
        CopyTransformation(1, 2),
        Transformation(
            query='''
DELETE {
    $output1 dmop:numberOfRows ?rows1.
    $output2 dmop:numberOfRows ?rows1.
}
INSERT {
    $output1 dmop:numberOfRows ?newRows1 .
    $output2 dmop:numberOfRows ?newRows2 .
}
WHERE {
    $output1 dmop:numberOfRows ?rows1.
    BIND(ROUND(?rows1 * (1 - $parameter1)) AS ?newRows1)
    BIND(?rows1 - ?newRows1 AS ?newRows2)
}
''',
        ),
    ],
)

label_extraction = Implementation(
    name='Label Extraction',
    algorithm=da.LabelExtraction,
    parameters=[
        Parameter('Label Column', XSD.string, None),
    ],
    input=[
        ds.LabeledTabularDatasetShape,
    ],
    output=[
        ds.UnlabeledTabularDatasetShape,
        ds.LabelDatasetShape,
    ],
    transformations=[
        CopyTransformation(1, 1),
        Transformation(
            query='''
DELETE {
    $output1 dmop:hasColumn ?column .
}
INSERT {
    $output2 dmop:hasColumn ?column .
}
WHERE {
    $output1 dmop:hasColumn ?column .
    ?column dmop:isLabel true .
}
'''
        ),
    ],
)
