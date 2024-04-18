from dataclasses import dataclass


@dataclass
class Recipe:
    recipe_name: str
    user_email: str
    difficulty: int
    instructions: str
    time_in_min: int
    ingredients_list: list
    id: int = None
