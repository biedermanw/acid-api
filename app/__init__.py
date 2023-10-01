import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig

from app.routes.main import main as main_bp
from app.routes.auth import auth as auth_bp

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_name=None):
    config_name = config_name or os.environ.get('FLASK_ENV', 'production')
    print(config_name)
    app = Flask(__name__)
    CORS(app)

    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(ProductionConfig)

    db.init_app(app)
    login.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    migrate.init_app(app, db)

    return app
