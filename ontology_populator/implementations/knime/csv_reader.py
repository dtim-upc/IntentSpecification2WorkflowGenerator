from ontology_populator.implementations.core import *
from common import *
from ontology_populator.implementations.core.transformation import LoaderTransformation
from ontology_populator.implementations.knime import KnimeImplementation, KnimeParameter, KnimeBaseBundle

csv_reader_implementation = KnimeImplementation(
    name='CSV Reader',
    algorithm=da.DataLoading,
    parameters=[
        KnimeParameter("File", XSD.string, '$$CSV_PATH$$', 'path', path='model/settings/file_selection/path'),
        KnimeParameter("Location flag", XSD.boolean, True, 'location_present',
                       path='model/settings/file_selection/path'),
        KnimeParameter("Filesystem", XSD.string, None, 'file_system_type', path='model/settings/file_selection/path'),

        KnimeParameter("FSI SettingsModelID", XSD.string, 'SMID_ReaderFileChooser', 'SettingsModelID',
                       path='model/settings/file_selection_Internals'),
        KnimeParameter("FSI EnabledStatus", XSD.boolean, True, 'EnabledStatus',
                       path='model/settings/file_selection_Internals'),

        KnimeParameter("has_fs_port", XSD.boolean, False, 'has_fs_port',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("overwritten_by_variable", XSD.boolean, False, 'overwritten_by_variable',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("convenience_fs_category", XSD.string, 'LOCAL', 'convenience_fs_category',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("relative_to", XSD.string, 'knime.workflow', 'relative_to',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("mountpoint", XSD.string, 'LOCAL', 'mountpoint',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("spaceId", XSD.string, '', 'spaceId',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("spaceName", XSD.string, '', 'spaceName',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("custom_url_timeout", XSD.integer, 1000, 'custom_url_timeout',
                       path='model/settings/file_selection/file_system_chooser__Internals'),
        KnimeParameter("connected_fs", XSD.boolean, True, 'connected_fs',
                       path='model/settings/file_selection/file_system_chooser__Internals'),

        KnimeParameter("has_column_header", XSD.boolean, True, 'has_column_header', path='model/settings'),
        KnimeParameter("has_row_id", XSD.boolean, False, 'has_row_id', path='model/settings'),
        KnimeParameter("support_short_data_rows", XSD.boolean, False, 'support_short_data_rows',
                       path='model/settings'),
        KnimeParameter("skip_empty_data_rows", XSD.boolean, False, 'skip_empty_data_rows', path='model/settings'),
        KnimeParameter("prepend_file_idx_to_row_id", XSD.boolean, False, 'prepend_file_idx_to_row_id',
                       path='model/settings'),
        KnimeParameter("comment_char", XSD.string, '#', 'comment_char', path='model/settings'),
        KnimeParameter("column_delimiter", XSD.string, ',', 'column_delimiter', path='model/settings'),
        KnimeParameter("quote_char", XSD.string, '"', 'quote_char', path='model/settings'),
        KnimeParameter("quote_escape_char", XSD.string, '"', 'quote_escape_char', path='model/settings'),
        KnimeParameter("use_line_break_row_delimiter", XSD.boolean, True, 'use_line_break_row_delimiter',
                       path='model/settings'),
        KnimeParameter("row_delimiter", XSD.string, '%%00013%%00010', 'row_delimiter', path='model/settings'),
        KnimeParameter("autodetect_buffer_size", XSD.integer, 1048576, 'autodetect_buffer_size',
                       path='model/settings'),

        KnimeParameter("spec_merge_mode_Internals", XSD.string, 'UNION', 'spec_merge_mode_Internals',
                       path='model/advanced_settings'),
        KnimeParameter("fail_on_differing_specs", XSD.boolean, True, 'fail_on_differing_specs',
                       path='model/advanced_settings'),
        KnimeParameter("append_path_column_Internals", XSD.boolean, False, 'append_path_column_Internals',
                       path='model/advanced_settings'),
        KnimeParameter("path_column_name_Internals", XSD.string, 'Path', 'path_column_name_Internals',
                       path='model/advanced_settings'),
        KnimeParameter("limit_data_rows_scanned", XSD.boolean, True, 'limit_data_rows_scanned',
                       path='model/advanced_settings'),
        KnimeParameter("max_data_rows_scanned", XSD.long, 10000, 'max_data_rows_scanned',
                       path='model/advanced_settings'),
        KnimeParameter("save_table_spec_config_Internals", XSD.boolean, True, 'save_table_spec_config_Internals',
                       path='model/advanced_settings'),
        KnimeParameter("limit_memory_per_column", XSD.boolean, True, 'limit_memory_per_column',
                       path='model/advanced_settings'),
        KnimeParameter("maximum_number_of_columns", XSD.integer, 8192, 'maximum_number_of_columns',
                       path='model/advanced_settings'),
        KnimeParameter("quote_option", XSD.string, 'REMOVE_QUOTES_AND_TRIM', 'quote_option',
                       path='model/advanced_settings'),
        KnimeParameter("replace_empty_quotes_with_missing", XSD.boolean, True, 'replace_empty_quotes_with_missing',
                       path='model/advanced_settings'),
        KnimeParameter("thousands_separator", XSD.string, '%%00000', 'thousands_separator',
                       path='model/advanced_settings'),
        KnimeParameter("decimal_separator", XSD.string, '.', 'decimal_separator', path='model/advanced_settings'),

        KnimeParameter("skip_lines", XSD.boolean, False, 'skip_lines', path='model/limit_rows'),
        KnimeParameter("number_of_lines_to_skip", XSD.long, 1, 'number_of_lines_to_skip', path='model/limit_rows'),
        KnimeParameter("skip_data_rows", XSD.boolean, False, 'skip_data_rows', path='model/limit_rows'),
        KnimeParameter("number_of_rows_to_skip", XSD.long, 1, 'number_of_rows_to_skip', path='model/limit_rows'),
        KnimeParameter("limit_data_rows", XSD.boolean, False, 'limit_data_rows', path='model/limit_rows'),
        KnimeParameter("max_rows", XSD.long, 50, 'max_rows', path='model/limit_rows'),

        KnimeParameter("charset", XSD.string, None, 'charset', path='model/encoding'),

        KnimeParameter("FMI SettingsModelID", XSD.string, 'SMID_FilterMode', 'SettingsModelID',
                       path='model/settings/file_selection/filter_mode_Internals'),
        KnimeParameter("FMI EnabledStatus", XSD.boolean, True, 'EnabledStatus',
                          path='model/settings/file_selection/filter_mode_Internals'),

        KnimeParameter("filter_mode", XSD.string, 'FILE', 'filter_mode',
                          path='model/settings/file_selection/filter_mode'),
        KnimeParameter("include_subfolders", XSD.boolean, False, 'include_subfolders',
                            path='model/settings/file_selection/filter_mode'),

        KnimeParameter("filter_files_extension", XSD.boolean, False, 'filter_files_extension',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("files_extension_expression", XSD.string, '', 'files_extension_expression',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("files_extension_case_sensitive", XSD.boolean, False, 'files_extension_case_sensitive',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("filter_files_name", XSD.boolean, False, 'filter_files_name',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("files_name_expression", XSD.string, '*', 'files_name_expression',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("files_name_case_sensitive", XSD.boolean, False, 'files_name_case_sensitive',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("files_name_filter_type", XSD.string, 'WILDCARD', 'files_name_filter_type',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("include_hidden_files", XSD.boolean, False, 'include_hidden_files',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("include_special_files", XSD.boolean, True, 'include_special_files',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("filter_folders_name", XSD.boolean, False, 'filter_folders_name',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("folders_name_expression", XSD.string, '*', 'folders_name_expression',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("folders_name_case_sensitive", XSD.boolean, False, 'folders_name_case_sensitive',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("folders_name_filter_type", XSD.string, 'WILDCARD', 'folders_name_filter_type',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("include_hidden_folders", XSD.boolean, False, 'include_hidden_folders',
                            path='model/settings/file_selection/filter_mode/filter_options'),
        KnimeParameter("follow_links", XSD.boolean, True, 'follow_links',
                            path='model/settings/file_selection/filter_mode/filter_options'),
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