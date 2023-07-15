from common import *
from .knime_implementation import KnimeImplementation, KnimeBaseBundle, KnimeParameter
from ..core import *

svm_learner_implementation = KnimeImplementation(
    name='SVM Learner',
    algorithm=da.SVM,
    parameters=[
        KnimeParameter("Class column", XSD.string, "$$LABEL$$", 'classcol'),
        KnimeParameter("Overlapping Penalty", XSD.double, 1.0, 'c_parameter'),
        KnimeParameter("Bias", XSD.double, 1.0, 'kernel_param_Bias'),
        KnimeParameter("Power", XSD.double, 1.0, 'kernel_param_Power'),
        KnimeParameter("Gamma", XSD.double, 1.0, 'kernel_param_Gamma'),
        KnimeParameter("Kappa", XSD.double, 0.1, 'kernel_param_kappa'),
        KnimeParameter("Delta", XSD.double, 0.5, 'kernel_param_delta'),
        KnimeParameter("Sigma", XSD.double, 0.1, 'kernel_param_sigma'),
        KnimeParameter("Kernel type", XSD.string, None, 'kernel_type'),
    ],
    input=[
        [ds.LabeledTabularDatasetShape, ds.NormalizedTabularDatasetShape, ds.NonNullTabularDatasetShape],
    ],
    output=[
        ds.SVMModel,
    ],
    implementation_type=do.LearnerImplementation,
    knime_node_factory='org.knime.base.node.mine.svm.learner.SVMLearnerNodeFactory2',
    knime_bundle=KnimeBaseBundle,
)

polynomial_svm_learner_component = Component(
    name='Polynomial SVM Learner',
    implementation=svm_learner_implementation,
    overriden_parameters=[
        ('Kernel type', 'Polynomial'),
    ],
    exposed_parameters=[
        'Class column',
        'Overlapping Penalty',
        'Bias',
        'Power',
        'Gamma',
    ],
    transformations=[],
)

hypertangent_svm_learner_component = Component(
    name='HyperTangent SVM Learner',
    implementation=svm_learner_implementation,
    overriden_parameters=[
        ('Kernel type', 'HyperTangent'),
    ],
    exposed_parameters=[
        'Class column',
        'Overlapping Penalty',
        'Kappa',
        'Delta',
    ],
    transformations=[],
)

rbf_svm_learner_component = Component(
    name='RBF SVM Learner',
    implementation=svm_learner_implementation,
    overriden_parameters=[
        ('Kernel type', 'RBF'),
    ],
    exposed_parameters=[
        'Class column',
        'Overlapping Penalty',
        'Sigma',
    ],
    transformations=[],
)

svm_predictor_implementation = KnimeImplementation(
    name='SVM Predictor',
    algorithm=da.SVM,
    parameters=[
        KnimeParameter("Prediction column name", XSD.string, "Prediction ($$LABEL$$)", 'prediction column name'),
        KnimeParameter("Change prediction", XSD.boolean, False, 'change prediction'),
        KnimeParameter("Add probabilities", XSD.boolean, False, 'add probabilities'),
        KnimeParameter("Class probability suffix", XSD.string, "", 'class probability suffix'),
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
    knime_node_factory='org.knime.base.node.mine.svm.predictor2.SVMPredictorNodeFactory',
    knime_bundle=KnimeBaseBundle,
)

svm_predictor_component = Component(
    name='SVM Predictor',
    implementation=svm_predictor_implementation,
    transformations=[
        CopyTransformation(2, 1),
        Transformation(
            query='''
INSERT DATA {
    $output1 dmop:hasColumn _:labelColumn .
    _:labelColumn a dmop:Column ;
        dmop:isLabel true;
      dmop:hasName $parameter1.
}
            ''',
        ),
    ],
    counterpart=[
        polynomial_svm_learner_component,
        hypertangent_svm_learner_component,
        rbf_svm_learner_component,
    ],
)
