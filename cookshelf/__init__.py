from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Globally accessible libraries
db = SQLAlchemy()


def init_app(config_object='config.Config'):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object)

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from .ingredients.routes import ingredients

        # Register Blueprints
        app.register_blueprint(ingredients, url_prefix='/ingredients')

        return app
