from ontology_populator.implementations.core import *
from common import *
from ontology_populator.implementations.core.transformation import LoaderTransformation
from ontology_populator.implementations.knime import KnimeImplementation, KnimeParameter, KnimeBaseBundle

csv_reader_implementation = KnimeImplementation(
    name='CSV Reader',
    algorithm=da.DataLoading,
    parameters=[
        KnimeParameter("File", XSD.string, '$$CSV_PATH$$', 'path', path='model/settings/fileSelection/path'),
        KnimeParameter("Location flag", XSD.boolean, True, 'location_present',
                       path='model/settings/fileSelection/path'),
        KnimeParameter("Filesystem", XSD.string, None, 'file_system_type', path='model/settings/fileSelection/path'),

    ],
    input=[],
    output=[
        ds.TabularDataset,
    ],
    knime_node_factory='org.knime.base.node.io.filehandling.csv.reader.CSVTableReaderNodeFactory',
    knime_bundle=KnimeBaseBundle,
)

csv_reader_local_component = Component(
    name='CSV Local reader',
    implementation=csv_reader_implementation,
    transformations=[
        LoaderTransformation(),
    ],
    overriden_parameters=[
        ('Location flag', True),
        ('Filesystem', 'LOCAL'),
    ],
    exposed_parameters=[
        'File'
    ],
)
