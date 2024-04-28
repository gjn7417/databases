from dataclasses import dataclass

@dataclass
class RecipeRatingInfo:
    recipe_name: str
    average_rating: float
    number_of_reviews: int

    @classmethod
    def from_db_row(cls, row):
        return cls(recipe_name=row.recipe_name, average_rating=row.average_rating, number_of_reviews=row.number_of_reviews)