import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="This field cannot be left blank"
            )

    parser.add_argument('password',
            type=str,
            required=True,
            help="This field cannot be left blank"
            )

    def post(self):
        data = UserRegister.parser.parse_args()

        #avoid duplicate usernames:
        if UserModel.find_by_username(data['username']):
            return {"message": "That username already exisis"}, 400

        user = UserModel(**data)
        #user = UserModel(data['username'], data['password'])
        user.save_to_db()


        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()

        return {"message": "User created successfully"}, 201

#api.add_resource(UserRegister, '/auth')
