from flask import jsonify
from sqlalchemy import text

from cookshelf.ingredients.data_models.ingredient import Ingredient


class IngredientDAO:
    def __init__(self, db):
        self.db = db

    def get_all_ingredients(self):
        sql = text("SELECT * FROM Ingredients")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return_dict = [Ingredient.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)

    def create_ingredient(self, ingredient: Ingredient):
        sql = text(f"""
                INSERT INTO Ingredients (name, food_category)
                VALUES (:name, :food_category)
            """)
        try:
            self.db.session.execute(sql, {'name': ingredient.name, 'food_category': ingredient.food_category})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def delete_ingredient(self, ingredient_id: int):
        sql = text(f"""
                CALL DeleteIngredient(:id)
            """)
        try:
            self.db.session.execute(sql, {'id': ingredient_id})
            self.db.session.commit()
            return jsonify({"success": True}), 204
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def update_ingredient(self, ingredient: Ingredient):
        sql = text(f"""
                UPDATE Ingredients
                SET 
                name = :name, 
                food_category = :food_category
                WHERE id = :id
            """)
        try:
            self.db.session.execute(sql, {'id': ingredient.id, 'name': ingredient.name,
                                          'food_category': ingredient.food_category})
            self.db.session.commit()
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def add_ingredients_to_recipe(self, recipe_id: int, ingredients: list[Ingredient]):
        print(f"Adding ingredients to recipe {recipe_id}, ingredients: {ingredients}")
        sql = text(f"""
                INSERT INTO Recipe_Ingredient (recipe_id, ingredient_id)
                VALUES (:recipe_id, :ingredient_id)
            """)
        try:
            for ingredient in ingredients:
                self.db.session.execute(sql, {'recipe_id': recipe_id, 'ingredient_id': ingredient['id']})
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def get_ingredients_by_id(self, id_list: list):
        sql = text(f"""
                SELECT * FROM Ingredients
                WHERE id IN :id_list
            """)
        try:
            result = self.db.session.execute(sql, {'id_list': id_list}).fetchall()
            self.db.session.commit()
            return_dict = [Ingredient.from_db_row(row).__dict__ for row in result]
            return jsonify(return_dict)
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def delete_recipe_ingredient_mapping(self, recipe_id: int, ingredient_id: int):
        sql = text(f"""
                DELETE FROM Recipe_Ingredient
                WHERE recipe_id = :recipe_id AND ingredient_id = :ingredient_id
            """)
        try:
            self.db.session.execute(sql, {'recipe_id': recipe_id, 'ingredient_id': ingredient_id})
            self.db.session.commit()
            return jsonify({"success": True}), 204
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def delete_all_recipe_ingredient_mappings(self, recipe_id: int):
        sql = text(f"""
                DELETE FROM Recipe_Ingredient
                WHERE recipe_id = :recipe_id
            """)
        try:
            self.db.session.execute(sql, {'recipe_id': recipe_id})
            self.db.session.commit()
            return jsonify({"success": True}), 204
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def bulk_update_ingredients_on_recipe(self, recipe_id: int, ingredients: list[Ingredient]):
        self.delete_all_recipe_ingredient_mappings(recipe_id)
        self.add_ingredients_to_recipe(recipe_id, ingredients)
        return jsonify({"success": True}), 200
