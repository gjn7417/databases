from flask import Blueprint, request

from cookshelf import db
from cookshelf.many_relations.many_dao import ManyDAO

many = Blueprint('many', __name__)
many_dao = ManyDAO(db)


@many.route('/get-recipe-tools', methods=['GET'])
def get_recipe_tools():
    return many_dao.get_recipe_tools()


@many.route('/update-recipe-tool', methods=['PUT'])
def update_recipe_tool():
    data = request.get_json()
    return many_dao.update_recipe_tool(data['recipe_id'], data['tool_id'], data['new_recipe_id'], data['new_tool_id'])


@many.route('/get-recipe-ingredients', methods=['GET'])
def get_recipe_ingredients():
    return many_dao.get_recipe_ingredients()


@many.route('/update-recipe-ingredient', methods=['PUT'])
def update_recipe_ingredient():
    data = request.get_json()
    return many_dao.update_recipe_ingredient(data['recipe_id'], data['ingredient_id'], data['new_recipe_id'],
                                             data['new_ingredient_id'])
