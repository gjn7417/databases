from flask import Blueprint, jsonify, request, make_response
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

    return_dict = [{
        'id': row.id,
        'name': row.name,
        'food_category': row.food_category,
    } for row in result]

    return jsonify(return_dict)


@ingredients.route('/create-ingredient', methods=['POST'])
def create_ingredient():
    data = request.get_json()
    name = data['name']
    category = data['category']

    sql = text(f"""
            INSERT INTO Ingredients (name, food_category)
            VALUES (:name, :category)
        """)
    try:
        db.session.execute(sql, {'name': name, 'category': category})
        db.session.commit()
        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@ingredients.route('/delete-ingredient', methods=['DELETE'])
def delete_ingredient():
    ingredient_id = request.args.get('id')

    sql = text(f"""
            DELETE FROM Ingredients
            WHERE id = :id
        """)
    try:
        db.session.execute(sql, {'id': ingredient_id})
        db.session.commit()
        return jsonify({"success": True}), 204
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@ingredients.route('/update-ingredient', methods=['PUT'])
def update_ingredient():
    data = request.get_json()
    id = data['id']
    name = data['name']
    category = data['category']

    sql = text(f"""
            UPDATE Ingredients
            SET 
            name = :name, 
            food_category = :category
            WHERE id = :id
        """)
    try:
        db.session.execute(sql, {'id': id, 'name': name, 'category': category})
        db.session.commit()
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
