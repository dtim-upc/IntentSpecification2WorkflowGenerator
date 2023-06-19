from .implementation import *
from common import *

decision_tree_learner = Implementation(
    name='Decision Tree Learner',
    algorithm=da.DecisionTree,
    parameters=[
        Parameter('Max Depth', XSD.integer, 10),
        Parameter('Min Samples Split', XSD.integer, 2),
        Parameter('Min Samples Leaf', XSD.integer, 1),
        Parameter('Max Leaf Nodes', XSD.integer, None),
        Parameter('Min Weight Fraction Leaf', XSD.float, 0.0),
        Parameter('Max Features', XSD.string, None),
        Parameter('Random State', XSD.integer, None),
    ],
    input=[
        ds.LabeledTabularDatasetShape,
    ],
    output=[
        ds.DecisionTreeModel,
    ],
    transformations=[
    ],
    implementation_type=do.LearnerImplementation
)

decision_tree_predictor = Implementation(
    name='Decision Tree Predictor',
    algorithm=da.DecisionTree,
    parameters=[
        Parameter('Prediction column', XSD.string, None),
    ],
    input=[
        ds.DecisionTreeModel,
        ds.TabularDataset,
    ],
    output=[
        ds.LabeledTabularDatasetShape,
    ],
    transformations=[
        CopyTransformation(2, 1),
        Transformation(
            query='''
INSERT DATA {
    $output1 dmop:hasColumn _:labelColumn.
    _:labelColumn a dmop:Column;
    _:labelColumn dmop:isLabel true;
}
            ''',
        ),
    ],
    implementation_type=do.ApplierImplementation,
    counterpart=decision_tree_learner,
)
