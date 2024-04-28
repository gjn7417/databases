from dataclasses import dataclass


@dataclass
class RecipeTool:
    recipe_id: int
    tool_id: int

    @classmethod
    def from_db_row(cls, row):
        return cls(
            recipe_id=row.recipe_id,
            tool_id=row.tool_id
        )
