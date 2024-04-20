import logging

from flask import jsonify
from sqlalchemy import text

from cookshelf.ingredients.ingredients_dao import IngredientDAO
from cookshelf.recipes.data_models.recipe import Recipe


class RecipeDAO:
    def __init__(self, db, ingredient_dao: IngredientDAO = None):
        self.db = db
        self.ingredient_dao = ingredient_dao or IngredientDAO(db)

    def create_recipe(self, recipe: Recipe):
        sql = text(f"""
                INSERT INTO Recipes (recipe_name, user_email, difficulty, time_in_min, instructions)
                VALUES (:recipe_name, :user_email, :difficulty, :time_in_min, :instructions)
            """)
        try:
            self.db.session.execute(sql, {'recipe_name': recipe.recipe_name, 'user_email': recipe.user_email,
                                          'difficulty': recipe.difficulty, 'time_in_min': recipe.time_in_min,
                                          'instructions': recipe.instructions})
            self.db.session.commit()
            insert_id = self.db.session.execute(text("SELECT LAST_INSERT_ID();")).scalar()
            print(f"Recipe created with id: {insert_id}")
            self.ingredient_dao.add_ingredients_to_recipe(recipe_id=insert_id, ingredients=recipe.ingredients_list)
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def update_recipe(self, recipe: Recipe):
        sql = text(f"""
                    UPDATE Recipes
                    SET recipe_name = :recipe_name, user_email = :user_email, difficulty = :difficulty, time_in_min = :time_in_min, instructions = :instructions
                    WHERE id = :id
                """)
        try:
            self.db.session.execute(sql, {'recipe_name': recipe.recipe_name, 'user_email': recipe.user_email,
                                          'difficulty': recipe.difficulty, 'time_in_min': recipe.time_in_min,
                                          'instructions': recipe.instructions, 'id': recipe.id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def get_recipe_reviews(self, recipe_id: int):
        sql = text(f"""
                SELECT * FROM Recipe_Reviews
                WHERE recipe_id = :recipe_id
            """)
        result = self.db.session.execute(sql, {'recipe_id': recipe_id}).fetchall()
        self.db.session.commit()

        return_dict = [Recipe.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)

    def get_all_recipes(self):
        sql = text("SELECT * FROM Recipes")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return_dict = [Recipe.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)
