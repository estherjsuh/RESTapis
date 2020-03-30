#import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') #lazy changes 'items' list to a query builder that has ability to look into items table 

    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #this is same as: SELECT * FROM

    def save_to_db(self): #this does the same thing as update AND insert
        db.session.add(self) #the session in this case is a collection of objects to write to DB
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
