from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    if isinstance(config_class, dict):
        app.config.update(config_class)
    else:
        app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import api

    app.register_blueprint(api)
    return app
