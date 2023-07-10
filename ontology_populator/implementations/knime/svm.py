from common import *
from ..core import *

svm_learner_implementation = Implementation(
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
    implementation_type=do.LearnerImplementation
)

svm_learner_component = Component(
    name='SVM Learner',
    implementation=svm_learner_implementation,
    transformations=[],
)

svm_predictor_implementation = Implementation(
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
    implementation_type=do.ApplierImplementation,
    counterpart=svm_learner_implementation,
)

svm_predictor_component = Component(
    name='SVM Predictor',
    implementation=svm_learner_implementation,
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
    counterpart=svm_learner_component,
)
