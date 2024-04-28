from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum


class Operation(Enum):
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'


@dataclass
class UsersAudit:
    audit_id: int
    email: str
    changed_at: datetime
    operation: Operation
    changed_data: str

    @classmethod
    def from_db_row(cls, row) -> 'UsersAudit':
        return cls(audit_id=row[0], email=row[1], changed_at=row[2], operation=Operation(row[3]), changed_data=row[4])

    def to_dict(self):
        result = asdict(self)
        result['operation'] = self.operation.name
        return result
