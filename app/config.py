# config.py contains the configuration settings for reading_nook
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

import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()


class Config:
    """
    Configuration class for the application.
    Attributes:
        SECRET_KEY (str): The secret key for the application.
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLite database.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to track modifications in the database.
        DEBUG (bool): Enables or disables debug mode.
    """
    SECRET_KEY = os.environ.get('READING_NOOK_SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///reading_nook.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1']


class DevelopmentConfig(Config):
    """
    Development configuration with debug enabled.
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Logs SQL queries for debugging purposes


class ProductionConfig(Config):
    """
    Production configuration with debug disabled.
    """
    DEBUG = False


class TestingConfig(Config):
    """
    Testing configuration with an in-memory SQLite database.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True
