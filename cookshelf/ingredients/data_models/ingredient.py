import dataclasses
from typing import Optional


@dataclasses.dataclass
class Ingredient:
    name: str
    food_category: str
    id: Optional[int] = None

    @classmethod
    def from_db_row(cls, row):
        return cls(id=row.id, name=row.name, food_category=row.food_category)