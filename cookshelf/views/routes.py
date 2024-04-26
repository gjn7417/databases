from flask import Blueprint

from cookshelf import db
from cookshelf.views.views_dao import RecipeIngredientDetailsDAO

views = Blueprint('views', __name__)

recipe_details_dao = RecipeIngredientDetailsDAO(db)


@views.route('/get-recipe-ingredient-details', methods=['GET'])
def get_all_recipe_details():
    return recipe_details_dao.get_all_recipe_details()


@views.route('/get-user-recipes', methods=['GET'])
def get_all_user_recipes():
    return recipe_details_dao.get_all_user_recipes()