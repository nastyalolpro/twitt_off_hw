from flask import Flask 

from twitt_off.models import db, migrate
from twitt_off.routes.home_routes import home_routes 
from twitt_off.routes.book_routes import book_routes
# from twitt_off.book_routes import book_routes

DATABASE_URL = "sqlite:///twittoff_8_development.db" # specify database url, using relative filepath


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # where does this database exits, or shoul dit exits when it gets created
    db.init_app(app) # configure app to know about the database
    migrate.init_app(app, db) # configure apps ability to hook into migrate command

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)