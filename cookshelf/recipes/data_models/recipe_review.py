import dataclasses


@dataclasses.dataclass
class RecipeReview:
    id: int
    text: str
    rating: int
    recipe_id: int

    @classmethod
    def from_db_row(cls, row):
        return cls(id=row.id, text=row.text, rating=row.rating, recipe_id=row.recipe_id)
