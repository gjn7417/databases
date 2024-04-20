from dataclasses import dataclass

from cookshelf.ingredients.data_models.ingredient import Ingredient


@dataclass
class Recipe:
    recipe_name: str
    user_email: str
    difficulty: int
    instructions: str
    time_in_min: int
    ingredients_list: list[Ingredient] = None
    id: int = None

    @classmethod
    def from_db_row(cls, row):
        return cls(recipe_name=row.recipe_name, user_email=row.user_email, difficulty=row.difficulty,
                   instructions=row.instructions, time_in_min=row.time_in_min, id=row.id)
