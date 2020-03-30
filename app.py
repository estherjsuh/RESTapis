from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity #2 important functions
from resources.user import UserRegister #will look at resources pkg/folder
from resources.item import Item, ItemList
from resources.store import Store, StoreList #if we don't import this, the table for store will not be created

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'zoey' #don't publish with this
api = Api(app)

#before first request runs, this will run; and create the data.db file
#this removes the create_table.py script


jwt = JWT(app, authenticate, identity) #jwt creates new endpoint, /auth

api.add_resource(Item, '/item/<string:name>') #same as doing @app.route('/student/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

#we only want to run flask app when we say 'python app.py'
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
