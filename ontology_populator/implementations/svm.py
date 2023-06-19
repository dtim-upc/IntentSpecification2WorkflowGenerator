from .implementation import *
from common import *

svm_learner = Implementation(
    name='SVM Learner',
    algorithm=da.SVM,
    parameters=[
        Parameter('Overlapping Penalty', XSD.float, 1.0),
        Parameter('Kernel', XSD.string, None),
    ],
    input=[
        [ds.LabeledTabularDatasetShape, ds.NormalizedTabularDatasetShape],
    ],
    output=[
        ds.SVMModel,
    ],
    transformations=[
    ],
    implementation_type=do.LearnerImplementation
)

svm_predictor = Implementation(
    name='SVM Predictor',
    algorithm=da.SVM,
    parameters=[
        Parameter('Prediction column', XSD.string, None),
    ],
    input=[
        ds.SVMModel,
        ds.NormalizedTabularDatasetShape,
    ],
    output=[
        ds.LabeledTabularDatasetShape,
    ],
    transformations=[
        CopyTransformation(2, 1),
        Transformation(
            query='''
INSERT DATA {
    $output1 dmop:hasColumn _:labelColumn .
    _:labelColumn a dmop:Column ;
        dmop:isLabel true .
}
            ''',
        ),
    ],
    implementation_type=do.ApplierImplementation,
    counterpart=svm_learner,
)
