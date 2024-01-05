# api/resources.py
from flask_restful import Resource, reqparse
from ..main.models import db, Members


class MembersResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lead', type=dict, required=True, help='Lead information is required')
        parser.add_argument('membership', type=dict, required=True, help='Membership information is required')

        args = parser.parse_args()

        try:
            # Extract lead information
            lead_data = args['lead']
            # Extract membership information
            membership_data = args['membership']
            lead = Members(
                first_name=lead_data['first_name'],
                last_name=lead_data['last_name'],
                email=lead_data['email'],
                program=membership_data['membership_name'],
                access=membership_data['level_name']
            )
            # Add and commit to the database
            db.session.add(lead)
            db.session.commit()

            return {'message': 'Member added successfully'}, 201  # 201 Created status code

        except Exception as e:
            db.session.rollback()
            return {'error': f'Failed to add member. Reason: {str(e)}'}, 500  # 500 Internal Server Error status code
    def get(self):
        return {"data": "Hello world"}