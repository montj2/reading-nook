# models.py database models for reading-nook
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

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin  # For user authentication
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """
    Represents a user in reading-nook.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password_hash (str): The hashed password of the user.
        articles (list): The articles associated with the user.

    Methods:
        set_password(password): Sets the password for the user.
        check_password(password): Checks if the provided password matches the user's password.

    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    articles = db.relationship('Article', backref='user', lazy=True)

    def set_password(self, password):
        """Sets the user's password with a hash, enforcing complexity."""
        if len(password) < 8 or not any(char.isdigit() for char in password):
            raise ValueError("Password must be at least 8 characters long and contain at least one number.")
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)


class Article(db.Model):
    """
    Represents an article.

    Attributes:
        id (int): The unique identifier for the article.
        url (str): The URL of the article.
        title (str): The title of the article.
        content (str): The content of the article.
        publication_date (datetime): The publication date of the article.
        author (str): The author of the article.
        user_id (int): The FK of the user who created the article.
        tags (list[Tag]): The tags associated with the article.
    """

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), unique=True, nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = db.relationship('Tag', secondary='article_tags', backref=db.backref('articles', lazy=True))


class Tag(db.Model):
    """
    Represents a tag in the application.
    Attributes:
        id (int): The unique identifier for the tag.
        name (str): The name of the tag.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)

    @classmethod
    def create_or_get(cls, tag_name):
        """Creates or retrieves a tag with a normalized name."""
        normalized_name = tag_name.strip().lower()
        tag = cls.query.filter_by(name=normalized_name).first()
        if tag is None:
            tag = cls(name=normalized_name)
            db.session.add(tag)
            db.session.commit()
        return tag


# Association table for many-to-many relationship between Article and Tag
article_tags = db.Table('article_tags',
                        db.Column('article_id',
                                  db.Integer,
                                  db.ForeignKey('article.id'),
                                  primary_key=True),
                        db.Column('tag_id',
                                  db.Integer,
                                  db.ForeignKey('tag.id'),
                                  primary_key=True)
)