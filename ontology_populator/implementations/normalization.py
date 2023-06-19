from .implementation import *
from common import *

min_max_scaling = Implementation(
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
    implementation_type=do.LearnerImplementation,
)

min_max_scaling_applier = Implementation(
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
    implementation_type=do.ApplierImplementation,
    counterpart=min_max_scaling
)

z_score_scaling = Implementation(
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
    implementation_type=do.LearnerImplementation,
)
z_score_scaling_applier = Implementation(
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
    implementation_type=do.ApplierImplementation,
    counterpart=z_score_scaling
)
