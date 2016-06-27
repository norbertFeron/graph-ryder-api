import uuid
from flask_restful import Resource, reqparse
from routes.utils import makeResponse
from graphtulip.degreeOfInterest import create

parser = reqparse.RequestParser()


class ComputeDOI(Resource):
    def get(self, type, id):
        graph_id = uuid.uuid4()
        create("complete", graph_id, type, id)
        return makeResponse([graph_id.urn[9:]])


class ComputeSearchDOI(Resource):
    def get(self, graph, type, id):
        params = []
        parser.add_argument('max_size', type=int)
        args = parser.parse_args()
        graph_id = uuid.uuid4()
        if args['max_size']:
            create(graph, graph_id, type, id, args['max_size'])
        else:
            create(graph, graph_id, type, id)
        return makeResponse([graph_id.urn[9:]])


class ComputeUserDOI(Resource):
    def get(self, type, id):
        graph_id = uuid.uuid4()
        create("usersToUsers", graph_id, type, id)
        return makeResponse([graph_id.urn[9:]])
