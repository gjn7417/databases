from flask import Blueprint, jsonify
from sqlalchemy import text

from cookshelf import db

ingredients = Blueprint('ingredients', __name__)


@ingredients.route('/')
def ingredient_home():
    return "Home Page for Ingredients"


@ingredients.route('/get-all-ingredients')
def get_all_ingredients():
    sql = text("SELECT * FROM Ingredients")
    result = db.session.execute(sql).fetchall()
    db.session.commit()

    return_dict = {
        "data": [{
            'id': row.id,
            'name': row.name,
            'food_category': row.food_category,
        } for row in result]
    }

    return jsonify(return_dict)
