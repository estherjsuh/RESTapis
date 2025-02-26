#import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #joining the items with stores
    store = db.relationship('StoreModel')

    def __init__(self,name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #this is same as: SELECT * FROM ITEMS WHERE name = name limit 1

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items where name = ?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        #
        # if row:
        #     return cls(*row)

    def save_to_db(self): #this does the same thing as update AND insert
        db.session.add(self) #the session in this case is a collection of objects to write to DB
        db.session.commit()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES (?,?)"
        # cursor.execute(query, (self.name, self.price))
        #
        # connection.commit()
        # connection.close()

    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query,(self.price, self.name))
    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
