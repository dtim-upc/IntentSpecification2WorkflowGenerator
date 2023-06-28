from ontology_populator.implementations.core import *
from common import *

catch_errors_data_ports = Implementation(
    name='Catch Errors (Data Ports)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Always populate error variables', None, None), # TODO: check parameter
        Parameter('Default for FailingNode variable:', None, None), # TODO: check parameter
        Parameter('Default for FailingNodeMessage variable:', None, None), # TODO: check parameter
        Parameter('Default for FailingNodeStackTrace variable:', None, None), # TODO: check parameter
        Parameter('Propagate Variables', None, None), # TODO: check parameter
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

catch_errors_generic_ports = Implementation(
    name='Catch Errors (Generic Ports)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Always populate error variables', None, None), # TODO: check parameter
        Parameter('Default for FailingNode variable:', None, None), # TODO: check parameter
        Parameter('Default for FailingNodeMessage variable:', None, None), # TODO: check parameter
        Parameter('Default for FailingNodeStackTrace variable:', None, None), # TODO: check parameter
        Parameter('Propagate Variables', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.PortObject'
        None, # TODO: check input, original: 'org.knime.core.node.port.PortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.PortObject'
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

catch_errors_var_ports = Implementation(
    name='Catch Errors (Var Ports)',
    algorithm=None, # TODO: check algorithm
    parameters=[
        Parameter('Always populate error variables', None, None), # TODO: check parameter
        Parameter('Default for FailingNode variable:', None, None), # TODO: check parameter
        Parameter('Default for FailingNodeMessage variable:', None, None), # TODO: check parameter
        Parameter('Default for FailingNodeStackTrace variable:', None, None), # TODO: check parameter
        Parameter('Propagate Variables', None, None), # TODO: check parameter
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

try_data_ports = Implementation(
    name='Try (Data Ports)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        ds.TabularDataset, # TODO: check input, original: 'org.knime.core.node.BufferedDataTable'
    ],
    output=[
        ds.TabularDataset, # TODO: check output, original: 'org.knime.core.node.BufferedDataTable'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

try_variable_ports = Implementation(
    name='Try (Variable Ports)',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

active_branch_inverter = Implementation(
    name='Active Branch Inverter',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
