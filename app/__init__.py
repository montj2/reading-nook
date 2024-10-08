# __init__.py -- Initialize the reading-nook application
"""
ISC License (ISC)

Copyright (c) 2024 James Montgomery <james.montgomery@gmail.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from flask import Flask
from flask_migrate import Migrate
from .database import db
from .models import User, Article, Tag  # Import your models
from .config import Config

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize the database and migration tools
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def hello():
        return "Welcome to Reading Nook!"

    with app.app_context():
        db.create_all()  # This is optional if you're using Flask-Migrate

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
