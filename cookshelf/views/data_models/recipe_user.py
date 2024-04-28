from dataclasses import dataclass

@dataclass
class UserRecipes:
    email: str
    first_name: str
    last_name: str
    user_name: str
    recipe_id: int
    recipe_name: str
    difficulty: int
    time_in_min: int
    instructions: str

    @classmethod
    def from_db_row(cls, row):
        return cls(
            email=row.email,
            first_name=row.first_name,
            last_name=row.last_name,
            user_name=row.user_name,
            recipe_id=row.recipe_id,
            recipe_name=row.recipe_name,
            difficulty=row.difficulty,
            time_in_min=row.time_in_min,
            instructions=row.instructions
        )