from flask import Blueprint, jsonify, request
from sqlalchemy import text

from cookshelf import db
from cookshelf.recipes.recipe import Recipe

recipes = Blueprint('recipes', __name__)


@recipes.route('/create-recipe', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe = Recipe(**data)

    sql = text(f"""
            INSERT INTO Recipes (recipe_name, user_email, difficulty, time_in_min, instructions)
            VALUES (:recipe_name, :user_email, :difficulty, :time_in_min, :instructions)
        """)
    try:
        db.session.execute(sql, {'recipe_name': recipe.recipe_name, 'user_email': recipe.user_email,
                                 'difficulty': recipe.difficulty, 'time_in_min': recipe.time_in_min,
                                 'instructions': recipe.instructions})
        db.session.commit()
        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
