"""Main application file"""

from create import log
try:
    from models import db
    from env import get_env
    from waitress import serve
    from create import api, app
    from sqlalchemy_utils import database_exists, create_database
except ImportError as e: log.error("Import error - %s", e); raise

from controllers.example_controller import ExampleGetPost
from controllers.index_controller import Index
api.add_resource(ExampleGetPost, '/example')
api.add_resource(Index, '/')

with app.app_context():
    try:
        db.init_app(app)
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
        db.create_all()
    except Exception as e:
        log.error("Database error - %s", e); raise

if __name__ == '__main__':
    log.debug("Starting Flask app")
    #serve(app, host=get_env("HOST_ADDRESS"), port=get_env("HOST_PORT"))
    print("Starting app")
    print(get_env("HOST_PORT"))
    print(get_env("HOST_ADDRESS"))
    print(get_env("DATABASE_URl"))
    print("#" * 100)
    app.run(debug=True, port=get_env("HOST_PORT"), host=get_env("HOST_ADDRESS"))
