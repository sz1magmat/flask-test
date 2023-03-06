"""Flask app creation with configuration"""

import logging
log = logging.getLogger(__name__)

logging.basicConfig(
    filemode='w',
    filename='app.log',
    level=logging.DEBUG,
    datefmt='%d-%b-%y %H:%M:%S',
    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    from env import get_env
    from flask import Flask
    from flask_cors import CORS
    from flask_restful import Api
except ImportError as e: logging.error("Import error - %s", e); raise

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = get_env("DATABASE_URL")

CORS(app)
api = Api(app)
log.debug("Flask app created with basic configuration")
