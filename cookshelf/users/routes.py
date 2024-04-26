from flask import Blueprint, request

from cookshelf import db
from cookshelf.users.data_models.User import User
from cookshelf.users.users_dao import UsersDAO

users = Blueprint('users', __name__)


@users.route('/get-users')
def get_users():
    users_dao = UsersDAO(db)
    return users_dao.get_all_users()


@users.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    users_dao = UsersDAO(db)
    return users_dao.create_user(user=user)


@users.route('/delete-user', methods=['DELETE'])
def delete_user():
    email = request.args.get('email')
    users_dao = UsersDAO(db)
    return users_dao.delete_user(email=email)


@users.route('/update-user', methods=['PUT'])
def update_user():
    data = request.get_json()
    user = User(**data)
    users_dao = UsersDAO(db)
    return users_dao.update_user(user=user)
