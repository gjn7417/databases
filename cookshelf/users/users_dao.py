from flask import jsonify
from sqlalchemy import text

from cookshelf.users.data_models.User import User

class UsersDAO:
    def __init__(self, db):
        self.db = db

    def get_all_users(self):
        sql = text("SELECT * FROM Users")
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return_dict = [User.from_db_row(row).__dict__ for row in result]

        return jsonify(return_dict)

    def create_user(self, user: User):
        sql = text(f"""
                INSERT INTO Users (email, first_name, last_name, user_name)
                VALUES (:email, :first_name, :last_name, :user_name)
            """)
        try:
            self.db.session.execute(sql, {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_name': user.user_name
            })
            self.db.session.commit()
            return jsonify({"success": True}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def delete_user(self, email: str):
        sql = text(f"""
                CALL DeleteUser(:email)
            """)
        try:
            self.db.session.execute(sql, {'email': email})
            self.db.session.commit()
            return jsonify({"success": True}), 204
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    def update_user(self, user: User):
        sql = text(f"""
                UPDATE Users
                SET 
                first_name = :first_name, 
                last_name = :last_name, 
                user_name = :user_name
                WHERE email = :email
            """)
        try:
            self.db.session.execute(sql, {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_name': user.user_name
            })
            self.db.session.commit()
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400
