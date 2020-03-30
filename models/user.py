import sqlite3
from db import db

#make the classes extend the db model
#this UserModel is an API, not a RESTapi; interface for other parts of the program - such as writing to DB and retrieving from DB
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users where username=?"
        # result = cursor.execute(query, (username,)) #parameters need to be in the form of a tuple;
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        #     #user = cls(row[0], row[1], row[2]) #needs to match parameters in the init method
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users where id=?"
        # result = cursor.execute(query, (_id,)) #parameters need to be in the form of a tuple;
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        #     #user = cls(row[0], row[1], row[2]) #needs to match parameters in the init method
        # else:
        #     user = None
        #
        # connection.close()
        # return user
