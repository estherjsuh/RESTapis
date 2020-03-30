from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
#import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
        )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id"
        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404


#need same parameters as get
    def post(self, name):
        #if there is an item that matches the name, then don't create dup
        #this is a error first approach
        if ItemModel.find_by_name(name):
            return {'message': "This item '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name,**data)
        #item = ItemModel(name,data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item."}, 500 #server error
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item Deleted'}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "DELETE FROM items where name = ?"
        # cursor.execute(query, (name,))
        # connection.commit()
        # connection.close()
        # return {"message":"Item deleted."}

    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name,**data)

        item.save_to_db()
        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        #above is same as: [x.json() for x in ItemModel.query.all()]
