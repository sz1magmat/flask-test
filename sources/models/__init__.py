"""Database creation"""

from create import log
try:
    from sqlalchemy import exc
    from flask_sqlalchemy import SQLAlchemy
except ImportError as e: log.error("Import error - %s", e); raise

try: log.debug("Creating database"); db = SQLAlchemy()
except exc.SQLAlchemyError as e: log.error("Failed to create database - %s", e); raise
