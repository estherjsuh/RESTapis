from werkzeug.security import safe_str_cmp
from models.user import UserModel

users = [
    UserModel('bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = UserModel.find_by_username(username) #this will return the id, username, password; if there isn't that username, returns None
    if user and safe_str_cmp(user.password, password):
        #same as safe_user.password == password, but safer
        return user #this generates the JWT token

def identity(payload):
    #payload is the contents of the JWT token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
