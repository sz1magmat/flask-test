"""Controller logic for index routes"""

from create import log
try: from flask_restful import Resource
except ImportError as e: log.error("Import error - %s", e); raise

class Index(Resource):
    """Index handler"""
    def get(self):
        """Get index message"""
        log.info('Getting index message')
        return {'message': 'Hello World'}, 200
