from flask import Blueprint, jsonify, request
from sqlalchemy import text

from cookshelf import db

users = Blueprint('users', __name__)

@users.route('/get-users')
def get_users():
    sql = text("SELECT * FROM Users")
    result = db.session.execute(sql).fetchall()
    db.session.commit()

    return_dict = [{
        'first_name': row.first_name,
        'last_name': row.last_name,
        'email': row.email,
        'user_name': row.user_name,
    } for row in result]

    return jsonify(return_dict)

@users.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    user_name = data['user_name']

    sql = text(f"""
                INSERT INTO Users (email, first_name, last_name, user_name)
                VALUES (:email, :fist_name, :last_name, :user_name)
            """)
    try:
        db.session.execute(sql, {
            'first_name': first_name, 'last_name': last_name, 'email': email, 'user_name': user_name})
        db.session.commit()
        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400