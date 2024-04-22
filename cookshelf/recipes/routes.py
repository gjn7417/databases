from flask import Blueprint, request

from cookshelf import db
from cookshelf.recipes.data_models.recipe import Recipe
from cookshelf.recipes.data_models.recipe_review import RecipeReview
from cookshelf.recipes.recipe_dao import RecipeDAO

recipes = Blueprint('recipes', __name__)


@recipes.route('/create-recipe', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe = Recipe(**data)
    recipe_dao = RecipeDAO(db)
    return recipe_dao.create_recipe(recipe=recipe)


@recipes.route('/update-recipe', methods=['POST'])
def update_recipe():
    data = request.get_json()
    recipe = Recipe(**data)
    recipe_dao = RecipeDAO(db)
    return recipe_dao.update_recipe(recipe=recipe)


@recipes.route('/get-recipe-reviews', methods=['GET'])
def get_recipe_reviews():
    recipe_id = int(request.args.get('id'))
    recipe_dao = RecipeDAO(db)
    return recipe_dao.get_recipe_reviews(recipe_id=recipe_id)


@recipes.route('/get-all-recipes', methods=['GET'])
def get_all_recipes():
    recipe_dao = RecipeDAO(db)
    return recipe_dao.get_all_recipes()


@recipes.route('/get-recipe-ingredients', methods=['GET'])
def get_recipe_ingredients():
    recipe_id = int(request.args.get('id'))
    recipe_dao = RecipeDAO(db)
    return recipe_dao.get_recipe_ingredients(recipe_id=recipe_id)


@recipes.route('/create-recipe-review', methods=['POST'])
def create_recipe_review():
    data = request.get_json()
    recipe_review = RecipeReview(**data)
    recipe_dao = RecipeDAO(db)
    return recipe_dao.create_recipe_review(recipe_review=recipe_review)

@recipes.route('/update-recipe-review', methods=['POST'])
def update_recipe_review():
    data = request.get_json()
    recipe_review = RecipeReview(**data)
    recipe_dao = RecipeDAO(db)
    return recipe_dao.update_recipe_review(recipe_review=recipe_review)

@recipes.route('/delete-recipe-review', methods=['DELETE'])
def delete_recipe_review():
    recipe_review_id = int(request.args.get('id'))
    recipe_dao = RecipeDAO(db)
    return recipe_dao.delete_recipe_review(recipe_review_id=recipe_review_id)
