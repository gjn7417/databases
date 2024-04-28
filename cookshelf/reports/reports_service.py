from sqlalchemy import text

from cookshelf.reports.data_models.recipe_rating import RecipeRatingInfo
from cookshelf.reports.data_models.user_activity import UserActivityInfo


class ReportsService:
    def __init__(self, db):
        self.db = db

    def get_avg_rating_of_recipe(self, recipe_id: int):
        sql = text(f"""
                SELECT AverageRecipeRating(:recipe_id)
            """)
        result = self.db.session.execute(sql, {'recipe_id': recipe_id}).fetchone()
        self.db.session.commit()

        return str(result[0])

    def get_user_recipe_count(self, user_email: str):
        sql = text(f"""
                SELECT CountUserRecipes(:user_email)
            """)
        result = self.db.session.execute(sql, {'user_email': user_email}).fetchone()
        self.db.session.commit()

        return str(result[0])

    def get_top_rated_recipes(self):
        sql = text(f"""
                SELECT 
                    Recipes.recipe_name, 
                    AVG(Recipe_Reviews.rating) AS average_rating, 
                    COUNT(Recipe_Reviews.id) AS number_of_reviews
                FROM 
                    Recipes
                JOIN 
                    Recipe_Reviews ON Recipes.id = Recipe_Reviews.recipe_id
                GROUP BY 
                    Recipes.id, Recipes.recipe_name
                ORDER BY 
                    average_rating DESC;
            """)
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return [RecipeRatingInfo.from_db_row(row) for row in result]

    def get_most_active_users(self):
        sql = text(f"""
                SELECT
                    Users.email,
                    COUNT(Recipes.id) AS number_of_recipes,
                    AVG(Recipe_Reviews.rating) AS average_rating
                FROM
                    Users
                JOIN
                    Recipes ON Users.email = Recipes.user_email
                JOIN
                    Recipe_Reviews ON Recipes.id = Recipe_Reviews.recipe_id
                GROUP BY
                    Users.email
                ORDER BY
                    number_of_recipes DESC;
            """)
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return [UserActivityInfo.from_db_row(row) for row in result]

    def get_least_rated_recipes(self):
        sql = text(f"""
                SELECT
                    Recipes.recipe_name,
                    AVG(Recipe_Reviews.rating) AS average_rating,
                    COUNT(Recipe_Reviews.id) AS number_of_reviews
                FROM
                    Recipes
                JOIN
                    Recipe_Reviews ON Recipes.id = Recipe_Reviews.recipe_id
                GROUP BY
                    Recipes.id, Recipes.recipe_name
                ORDER BY
                    average_rating ASC;
            """)
        result = self.db.session.execute(sql).fetchall()
        self.db.session.commit()

        return [RecipeRatingInfo.from_db_row(row) for row in result]
