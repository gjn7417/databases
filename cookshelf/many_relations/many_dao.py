from flask import jsonify
from sqlalchemy import text

from cookshelf.many_relations.data_models.recipe_ingredient import RecipeIngredient
from cookshelf.many_relations.data_models.recipe_tool import RecipeTool


class ManyDAO:
    def __init__(self, db):
        self.db = db

    def get_recipe_tools(self):
        try:
            sql = text(f"""
                    SELECT * FROM Recipe_Tools
                """)
            result = self.db.session.execute(sql).fetchall()
            self.db.session.commit()

            return [RecipeTool.from_db_row(row) for row in result]
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400


    def update_recipe_tool(self, recipe_id: int, tool_id: int, new_recipe_id: int, new_tool_id: int):
        try:
            sql = text(f"""
                    UPDATE Recipe_Tools
                    SET recipe_id = :new_recipe_id, tool_id = :new_tool_id
                    WHERE recipe_id = :recipe_id AND tool_id = :tool_id
                """)
            self.db.session.execute(sql, {'recipe_id': recipe_id, 'tool_id': tool_id, 'new_recipe_id': new_recipe_id, 'new_tool_id': new_tool_id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400


    def get_recipe_ingredients(self):
        try:
            sql = text(f"""
                    SELECT * FROM Recipe_Ingredient
                """)
            result = self.db.session.execute(sql).fetchall()
            self.db.session.commit()
            return [RecipeIngredient.from_db_row(row) for row in result]
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def update_recipe_ingredient(self, recipe_id: int, ingredient_id: int, new_recipe_id: int, new_ingredient_id: int):
        try:
            sql = text(f"""
                    UPDATE Recipe_Ingredient
                    SET recipe_id = :new_recipe_id, ingredient_id = :new_ingredient_id
                    WHERE recipe_id = :recipe_id AND ingredient_id = :ingredient_id
                """)
            self.db.session.execute(sql, {'recipe_id': recipe_id, 'ingredient_id': ingredient_id, 'new_recipe_id': new_recipe_id, 'new_ingredient_id': new_ingredient_id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400
