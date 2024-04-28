from flask import Blueprint, request

from cookshelf import db
from cookshelf.reports.reports_service import ReportsService

reports = Blueprint('reports', __name__)
reports_service = ReportsService(db)


@reports.route('/get-avg-rating-of-recipe', methods=['GET'])
def get_avg_rating_of_recipe():
    recipe_id = int(request.args.get('id'))
    return reports_service.get_avg_rating_of_recipe(recipe_id=recipe_id)


@reports.route('/get-user-recipe-count', methods=['GET'])
def get_user_recipe_count():
    user_email = request.args.get('email')
    return reports_service.get_user_recipe_count(user_email=user_email)


@reports.route('/get-top-rated-recipes', methods=['GET'])
def get_top_rated_recipes():
    return reports_service.get_top_rated_recipes()


@reports.route('/get-most-active-users', methods=['GET'])
def get_most_active_users():
    return reports_service.get_most_active_users()


@reports.route('/get-least-rated-recipes', methods=['GET'])
def get_least_rated_recipes():
    return reports_service.get_least_rated_recipes()
