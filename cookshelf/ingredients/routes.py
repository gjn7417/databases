from flask import Blueprint, jsonify, request, make_response
from sqlalchemy import text

from cookshelf import db
from cookshelf.ingredients.data_models.ingredient import Ingredient
from cookshelf.ingredients.ingredients_dao import IngredientDAO

ingredients = Blueprint('ingredients', __name__)


@ingredients.route('/get-all-ingredients')
def get_all_ingredients():
    ingredient_dao = IngredientDAO(db)
    return ingredient_dao.get_all_ingredients()


@ingredients.route('/create-ingredient', methods=['POST'])
def create_ingredient():
    data = request.get_json()
    ingredient = Ingredient(**data)
    ingredient_dao = IngredientDAO(db)
    return ingredient_dao.create_ingredient(ingredient=ingredient)


@ingredients.route('/delete-ingredient', methods=['DELETE'])
def delete_ingredient():
    ingredient_id = int(request.args.get('id'))
    ingredient_dao = IngredientDAO(db)
    return ingredient_dao.delete_ingredient(ingredient_id=ingredient_id)


@ingredients.route('/update-ingredient', methods=['PUT'])
def update_ingredient():
    data = request.get_json()
    ingredient = Ingredient(**data)
    ingredient_dao = IngredientDAO(db)
    return ingredient_dao.update_ingredient(ingredient=ingredient)
