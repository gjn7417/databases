from dataclasses import dataclass


@dataclass
class RecipeIngredient:
    recipe_id: int
    ingredient_id: int

    @classmethod
    def from_db_row(cls, row):
        return cls(
            recipe_id=row.recipe_id,
            ingredient_id=row.ingredient_id
        )
