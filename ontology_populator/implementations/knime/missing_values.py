from .knime_implementation import KnimeImplementation, KnimeParameter, KnimeBaseBundle
from ..core import *
from common import *

missing_value_implementation = KnimeImplementation(
    name='Missing Value',
    algorithm=da.MissingValueManagement,
    parameters=[
        KnimeParameter('Integer', XSD.string, None, 'factoryID',
                       path='model/dataTypeSettings/org.knime.core.data.def.IntCell', condition='$$INTEGER_COLUMN$$'),
        KnimeParameter('Float', XSD.string, None, 'factoryID',
                       path='model/dataTypeSettings/org.knime.core.data.def.StringCell', condition='$$STRING_COLUMN$$'),
        KnimeParameter('String', XSD.string, None, 'factoryID',
                       path='model/dataTypeSettings/org.knime.core.data.def.DoubleCell', condition='$$FLOAT_COLUMN$$'),
    ],
    input=[
        ds.TabularDataset,
    ],
    output=[
        ds.NonNullTabularDatasetShape,
        ds.MissingValueModel,
    ],
    implementation_type=do.LearnerImplementation,
    knime_node_factory='org.knime.base.node.preproc.pmml.missingval.compute.MissingValueHandlerNodeFactory',
    knime_bundle=KnimeBaseBundle,
)

mean_imputation_component = Component(
    name='Mean Imputation',
    implementation=missing_value_implementation,
    overriden_parameters=[
        ('Integer', 'org.knime.base.node.preproc.pmml.missingval.handlers.DoubleMeanMissingCellHandlerFactory'),
        ('Float', 'org.knime.base.node.preproc.pmml.missingval.handlers.DoubleMeanMissingCellHandlerFactory'),
        ('String', 'org.knime.base.node.preproc.pmml.missingval.handlers.MostFrequentValueMissingCellHandlerFactory'),
    ],
    exposed_parameters=[],
    transformations=[
        CopyTransformation(1, 1),
        Transformation(
            query='''
DELETE {
    ?column dmop:containsNulls false.
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?column dmop:containsNulls true.
}
'''),
    ],
)

drop_rows_component = Component(
    name='Drop Rows with Missing Values',
    implementation=missing_value_implementation,
    overriden_parameters=[
        ('Integer', 'org.knime.base.node.preproc.pmml.missingval.pmml.RemoveRowMissingCellHandlerFactory'),
        ('Float', 'org.knime.base.node.preproc.pmml.missingval.pmml.RemoveRowMissingCellHandlerFactory'),
        ('String', 'org.knime.base.node.preproc.pmml.missingval.pmml.RemoveRowMissingCellHandlerFactory'),
    ],
    exposed_parameters=[],
    transformations=[
        CopyTransformation(1, 1),
        Transformation(
            query='''
DELETE {
    ?column dmop:containsNulls false.
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?column dmop:containsNulls true.
}
'''),
        Transformation(
            query='''
DELETE {
    $output1 dmop:numberOfRows ?rows1.
}
WHERE {
    $output1 dmop:numberOfRows ?rows1.
}
''',
        ),
        Transformation(
            query='''
INSERT DATA {
    $output2 da:removesProperty dmop:numberOfRows.
}
''',
        ),
    ],
)

missing_value_applier_implementation = KnimeImplementation(
    name='Missing Value (Applier)',
    algorithm=da.MissingValueManagement,
    parameters=[
    ],
    input=[
        ds.MissingValueModel,
        ds.TabularDataset,
    ],
    output=[
        ds.NonNullTabularDatasetShape,
    ],
    implementation_type=do.ApplierImplementation,
    knime_node_factory='org.knime.base.node.preproc.pmml.missingval.apply.MissingValueApplyNodeFactory',
    knime_bundle=KnimeBaseBundle,
)

missing_value_applier_component = Component(
    name='Missing Value Management Applier',
    implementation=missing_value_applier_implementation,
    overriden_parameters=[],
    exposed_parameters=[],
    transformations=[
        CopyTransformation(2, 1),
        Transformation(
            query='''
DELETE {
    $output2 ?property ?value.
}
WHERE {
    $output1 da:removesProperty ?property.
    $output2 ?property ?value.
}
''',
        ),
    ],
    counterpart=[
        mean_imputation_component,
        drop_rows_component,
    ]
)
