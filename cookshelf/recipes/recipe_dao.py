import logging

from flask import jsonify
from sqlalchemy import text

from cookshelf.ingredients.ingredients_dao import IngredientDAO
from cookshelf.recipes.data_models.recipe import Recipe
from cookshelf.recipes.data_models.recipe_review import RecipeReview
from cookshelf.tools.tools_dao import ToolsDAO


class RecipeDAO:
    def __init__(self, db, ingredient_dao: IngredientDAO = None, tools_dao: ToolsDAO = None):
        self.db = db
        self.ingredient_dao = ingredient_dao or IngredientDAO(db)
        self.tools_dao = tools_dao or ToolsDAO(db)

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
            insert_id = self.db.session.execute(text("SELECT MAX(id) from Recipes;")).scalar()
            print(f"Recipe created with id: {insert_id}")
            self.ingredient_dao.add_ingredients_to_recipe(recipe_id=insert_id, ingredients=recipe.ingredients_list)
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def delete_recipe(self, recipe_id: int):
        sql = text(f"""
                    CALL DeleteRecipe(:id)
                """)
        try:
            self.db.session.execute(sql, {'id': recipe_id})
            self.db.session.commit()
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
            self.ingredient_dao.bulk_update_ingredients_on_recipe(recipe_id=recipe.id,
                                                                  ingredients=recipe.ingredients_list)
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

        return_dict = [RecipeReview.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)

    def get_all_recipes(self):
        sql = text("SELECT * FROM Recipes")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return_dict = [Recipe.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)

    def get_recipe_ingredients(self, recipe_id: int):
        sql = text(f"""
                SELECT * FROM Recipe_Ingredient
                WHERE recipe_id = :recipe_id
            """)
        result = self.db.session.execute(sql, {'recipe_id': recipe_id}).fetchall()
        self.db.session.commit()

        ingredient_ids = [item[1] for item in result]

        return self.ingredient_dao.get_ingredients_by_id(ingredient_ids)

    def create_recipe_review(self, recipe_review: RecipeReview):
        sql = text(f"""
                INSERT INTO Recipe_Reviews (text, rating, recipe_id)
                VALUES (:text, :rating, :recipe_id)
            """)
        try:
            self.db.session.execute(sql, {'text': recipe_review.text, 'rating': recipe_review.rating,
                                          'recipe_id': recipe_review.recipe_id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def update_recipe_review(self, recipe_review: RecipeReview):
        sql = text(f"""
                    UPDATE Recipe_Reviews
                    SET text = :text, rating = :rating
                    WHERE id = :id
                """)
        try:
            self.db.session.execute(sql, {'text': recipe_review.text, 'rating': recipe_review.rating,
                                          'id': recipe_review.id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def delete_recipe_review(self, recipe_review_id: int):
        sql = text(f"""
                    DELETE FROM Recipe_Reviews
                    WHERE id = :id
                """)
        try:
            self.db.session.execute(sql, {'id': recipe_review_id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400


    def add_recipe_tool(self, recipe_id: int, tool_id: int):
        sql = text(f"""
                    INSERT INTO Recipe_Tools (recipe_id, tool_id)
                    VALUES (:recipe_id, :tool_id)
                """)
        try:
            self.db.session.execute(sql, {'recipe_id': recipe_id, 'tool_id': tool_id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400


    def delete_recipe_tool(self, recipe_id: int, tool_id: int):
        sql = text(f"""
                    DELETE FROM Recipe_Tools
                    WHERE recipe_id = :recipe_id AND tool_id = :tool_id
                """)
        try:
            self.db.session.execute(sql, {'recipe_id': recipe_id, 'tool_id': tool_id})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def get_recipe_tools(self, recipe_id: int):
        sql = text(f"""
                SELECT * FROM Recipe_Tools
                WHERE recipe_id = :recipe_id
            """)
        result = self.db.session.execute(sql, {'recipe_id': recipe_id}).fetchall()
        self.db.session.commit()

        tools_ids = [item[1] for item in result]

        return self.tools_dao.get_tools_by_id(tools_ids)

