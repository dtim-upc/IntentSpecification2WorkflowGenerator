from ..core import *
from common import *

min_max_scaling_implementation = Implementation(
    name='Min-Max Scaling',
    algorithm=da.MinMaxScaling,
    parameters=[
        Parameter('Minimum', XSD.float, 0),
        Parameter('Maximum', XSD.float, 1),
    ],
    input=[
        ds.TabularDataset,
    ],
    output=[
        ds.NormalizedTabularDatasetShape,
        ds.MinMaxScalerModel,
    ],
    implementation_type=do.LearnerImplementation,
)

min_max_scaling_component = Component(
    name='Min-Max Scaling',
    implementation=min_max_scaling_implementation,

    transformations=[
        CopyTransformation(1, 1),
        Transformation(
            query='''
DELETE {
    ?column ?valueProperty ?value
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?valuePropetry rdfs:subPropertyOf dmop:ColumnValueInfo.
    ?column ?valueProperty ?value.
}
            ''',
        ),
        Transformation(
            query='''
INSERT {
    ?column dmop:hasMinValue $parameter1;
            dmop:hasMaxValue $parameter2.
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?column dmop:isFeature true ;
}
            ''',
        ),
        Transformation(
            query='''
INSERT DATA {
    $output1 dmop:isNormalized true.
}
            ''',
        ),
    ],
)

min_max_scaling_applier_implementation = Implementation(
    name='Min-Max Scaling Applier',
    algorithm=da.MinMaxScaling,
    parameters=[
        Parameter('Minimum', XSD.float, 0),
        Parameter('Maximum', XSD.float, 1),
    ],
    input=[
        ds.TabularDataset,
        ds.MinMaxScalerModel,
    ],
    output=[
        ds.NormalizedTabularDatasetShape,
    ],
    implementation_type=do.ApplierImplementation,
    counterpart=min_max_scaling_implementation
)

min_max_scaling_applier_component = Component(
    name='Min-Max Scaling Applier',
    implementation=min_max_scaling_applier_implementation,

    transformations=[
        CopyTransformation(1, 1),
        Transformation(
            query='''
DELETE {
    ?column ?valueProperty ?value
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?valuePropetry rdfs:subPropertyOf dmop:ColumnValueInfo.
    ?column ?valueProperty ?value.
}
            ''',
        ),
        Transformation(
            query='''
INSERT {
    ?column dmop:hasMinValue $parameter1;
            dmop:hasMaxValue $parameter2.
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?column dmop:isFeature true ;
}
            ''',
        ),
        Transformation(
            query='''
INSERT DATA {
    $output1 dmop:isNormalized true.
}
            ''',
        ),
    ],
    counterpart=min_max_scaling_component,
)

z_score_scaling_implementation = Implementation(
    name='Z-Score Scaling',
    algorithm=da.ZScoreScaling,
    parameters=[],
    input=[
        ds.TabularDataset,
    ],
    output=[
        ds.NormalizedTabularDatasetShape,
        ds.ZScoreScalerModel,
    ],
    implementation_type=do.LearnerImplementation,
)

z_score_scaling_component = Component(
    name='Z-Score Scaling',
    implementation=z_score_scaling_implementation,

    transformations=[
        CopyTransformation(1, 1),
        Transformation(
            query='''
DELETE {
    ?column ?valueProperty ?value
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?valuePropetry rdfs:subPropertyOf dmop:ColumnValueInfo.
    ?column ?valueProperty ?value.
}
            ''',
        ),
        Transformation(
            query='''
INSERT {
    ?column dmop:hasMeanValue 0;
            dmop:hasStandardDeviation 1.
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?column dmop:isFeature true ;
}
            ''',
        ),
        Transformation(
            query='''
INSERT DATA {
    $output1 dmop:isNormalized true.
}
            ''',
        ),
    ],
)

z_score_scaling_applier_implementation = Implementation(
    name='Z-Score Scaling Applier',
    algorithm=da.ZScoreScaling,
    parameters=[],
    input=[
        ds.TabularDataset,
        ds.ZScoreScalerModel,
    ],
    output=[
        ds.NormalizedTabularDatasetShape,
    ],
    implementation_type=do.ApplierImplementation,
    counterpart=z_score_scaling_implementation
)

z_score_scaling_applier_component = Component(
    name='Z-Score Scaling Applier',
    implementation=z_score_scaling_applier_implementation,

    transformations=[
        CopyTransformation(1, 1),
        Transformation(
            query='''
DELETE {
    ?column ?valueProperty ?value
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?valuePropetry rdfs:subPropertyOf dmop:ColumnValueInfo.
    ?column ?valueProperty ?value.
}
            ''',
        ),
        Transformation(
            query='''
INSERT {
    ?column dmop:hasMeanValue 0;
            dmop:hasStandardDeviation 1.
}
WHERE {
    $output1 dmop:hasColumn ?column.
    ?column dmop:isFeature true ;
}
            ''',
        ),
        Transformation(
            query='''
INSERT DATA {
    $output1 dmop:isNormalized true.
}
            ''',
        ),
    ],
    counterpart=z_score_scaling_component,
)
