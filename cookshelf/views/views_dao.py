from flask import jsonify
from sqlalchemy import text

from cookshelf.views.data_models.recipe_ingredient_detail import RecipeIngredientDetails
from cookshelf.views.data_models.recipe_user import UserRecipes


class RecipeIngredientDetailsDAO:
    def __init__(self, db):
        self.db = db

    def get_all_recipe_details(self):
        sql = text("SELECT * FROM RecipeIngredientDetails")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return_dict = [RecipeIngredientDetails.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)

    def get_all_user_recipes(self):
        sql = text("SELECT * FROM UserRecipes")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return_dict = [UserRecipes.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)
