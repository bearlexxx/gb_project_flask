from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_project.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    # print(__name__)
    app = Flask(__name__)  # app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from flask_project.main.routes import main
    from flask_project.users.routes import users
    from flask_project.posts.routes import posts
    from flask_project.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
