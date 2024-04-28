from dataclasses import dataclass


@dataclass
class RecipeIngredientDetails:
    id: int
    recipe_name: str
    user_email: str
    difficulty: int
    time_in_min: int
    instructions: str
    ingredient_id: int
    ingredient_name: str
    food_category: str

    @classmethod
    def from_db_row(cls, row):
        return cls(
            id=row.id,
            recipe_name=row.recipe_name,
            user_email=row.user_email,
            difficulty=row.difficulty,
            time_in_min=row.time_in_min,
            instructions=row.instructions,
            ingredient_id=row.ingredient_id,
            ingredient_name=row.ingredient_name,
            food_category=row.food_category
        )
