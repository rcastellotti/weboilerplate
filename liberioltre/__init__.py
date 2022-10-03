from flask import Flask
from liberioltre.main import main
from flask_login import LoginManager
from liberioltre.models import db, User, Product, Order
import stripe
import click
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object("liberioltre.config.Config")
    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "/admin/login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    stripe.api_key = app.config["STRIPE_API_KEY"]

    app.register_blueprint(main)
    # app.register_blueprint(admin, url_prefix="/admin")

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Product": Product, "Order": Order}

    @app.cli.command("createdb")
    def createdb():
        db.create_all()

    return app