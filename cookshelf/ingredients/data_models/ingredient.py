import dataclasses

@dataclasses.dataclass
class Ingredient:
    id: int
    name: str
    food_category: str

    @classmethod
    def from_db_row(cls, row):
        return cls(id=row.id, name=row.name, food_category=row.food_category)