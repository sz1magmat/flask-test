"""Controller logic for example routes"""

from create import log
try:
    from models.example import Example, db
    from flask_restful import Resource, reqparse
except ImportError as e: log.error("Import error - %s", e); raise

parser = reqparse.RequestParser()
parser.add_argument('message')

class ExampleGetPost(Resource):
    """Example handler"""

    def get(self):
        """Get all examples"""
        log.info('Getting examples')
        examples = Example.query.all()
        return [example.message for example in examples], 200

    def post(self):
        """Create a new example"""
        args = parser.parse_args()
        log.info('Creating a new example')
        example = Example(message=args['message'])

        db.session.add(example); db.session.commit()
        return f"Example created - {example.message}", 201
