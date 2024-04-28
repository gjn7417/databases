from dataclasses import dataclass


@dataclass
class Tool:
    id: int
    name: str
    brand: str

    @classmethod
    def from_db_row(cls, row):
        return cls(id=row.id, name=row.name, brand=row.brand)
