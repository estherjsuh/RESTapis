from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id"
            )

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):

        if StoreModel.find_by_name(name):
            return {'message': "This store '{}' already exists.".format(name)}, 400
        #if store does not exist:
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occurred inserting the item.'}, 500 #server error
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store Deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
