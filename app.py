from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import datetime

from security import authenticate, identity
from resources.user import UserRegister # work on importing the user UserRegister from user.py first 
from resources.item import Item, ItemList,SingleCrud
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # we can specify the type of database from sqlite to postgres and it should work out of the box
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disable SQLALCHEMy sessions to make code run faster we use Flask SQL ALCHEMY tracker
app.secret_key = 'thereisawoman'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()
    
jwt = JWT(app, authenticate, identity) # JWT creates a new end point, that is /auth
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=365) 


#items = []





api.add_resource(Item, '/item') # http://127.0.0.1:5000/birds/weidevogels
api.add_resource(SingleCrud, '/item/<string:name>') # http://127.0.0.1:5000/birds/weidevogels
api.add_resource(ItemList, '/items') # http://127.0.0.1:5000/birds/
api.add_resource(UserRegister, '/register') # http://127.0.0.1:5000/register/

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
