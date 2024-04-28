from dataclasses import dataclass

@dataclass
class UserActivityInfo:
    email: str
    number_of_recipes: int
    average_rating: float

    @classmethod
    def from_db_row(cls, row):
        return cls(email=row.email, number_of_recipes=row.number_of_recipes, average_rating=row.average_rating)