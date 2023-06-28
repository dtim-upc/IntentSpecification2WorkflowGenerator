from ontology_populator.implementations.core import *
from common import *

db_transaction_end = Implementation(
    name='DB Transaction End',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
        None, # TODO: check output, original: 'org.knime.core.node.port.flowvariable.FlowVariablePortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)

db_transaction_start = Implementation(
    name='DB Transaction Start',
    algorithm=None, # TODO: check algorithm
    parameters=[
    ],
    input=[
        None, # TODO: check input, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    output=[
        None, # TODO: check output, original: 'org.knime.database.port.DBSessionPortObject'
    ],
    implementation_type=do.Implementation # TODO: check implementation type
)
