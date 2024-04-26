from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Globally accessible libraries
db = SQLAlchemy()


def init_app(config_object='config.Config'):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object)

    # Allow Cross Origin Requests from LocalHost
    CORS(app, origins=["http://localhost:4200"], methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from .ingredients.routes import ingredients
        from .users.routes import users
        from cookshelf.recipes.routes import recipes
        from cookshelf.tools.routes import tools
        from cookshelf.views.routes import views

        # Register Blueprints
        app.register_blueprint(ingredients, url_prefix='/ingredients')
        app.register_blueprint(users, url_prefix='/users')
        app.register_blueprint(recipes, url_prefix='/recipes')
        app.register_blueprint(tools, url_prefix='/tools')
        app.register_blueprint(views, url_prefix='/views')

        return app
