import sqlite3
from flask_restful import  Resource, reqparse, request
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    

    parser = reqparse.RequestParser()
    parser.add_argument("features",
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

   


    def post(self):
        data = request.get_json() 
        idm = data["id"]
        date = data["date"]
        name = data["name"]
        telephone = data["telephone"]
        email = data["email"]
        categorie = data["categorie"]
        toelichting = data["toelichting"]
        XCoordinaat = data["XCoordinaat"]
        YCoordinaat = data["YCoordinaat"]
        image = data["image"]

        if ItemModel.find_by_name(idm):
            return{'message':'An item name: {} already exist'.format(idm)},400







        #cordinates = data["features"][0]['geometry']['coordinates']
        #Score = data["features"][0]['properties']['Score']
        #return {"message":idm}
        item =ItemModel(idm,date,name,telephone,email,categorie,toelichting,XCoordinaat,YCoordinaat,image)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"},500 #500 internal server error

        return item.json(), 201 # This returns the code for 201 which means created when the server creates data #202 is accepted delays creating items





    def put(self):
        data = request.get_json() 
        idm = data["id"]
        date = data["date"]
        name = data["name"]
        telephone = data["telephone"]
        email = data["email"]
        categorie = data["categorie"]
        toelichting = data["toelichting"]
        XCoordinaat = data["XCoordinaat"]
        YCoordinaat = data["YCoordinaat"]
        image = data["image"]

        item =ItemModel.find_by_name(idm)        
        updated_item = ItemModel(idm,date,name,telephone,email,categorie,toelichting,XCoordinaat,YCoordinaat,image)

        if item is None:
            item =ItemModel(idm,date,name,telephone,email,categorie,toelichting,XCoordinaat,YCoordinaat,image)
        else:
            item.name = name
            item.XCoordinaat = XCoordinaat
            item.YCoordinaat = YCoordinaat
        item.save_to_db()

        return updated_item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]} #list comprehension
        #{'items': list(map(lambda x:x.json(), ItemModel.query.all()))} lambda function 


class SingleCrud(Resource):
    #@jwt_required()
    def get(self, name):  
        item =ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'},404   

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'data deleted successfully'}

class Categorie(Resource):
        def get(self, categorie):  
            item =ItemModel.find_by_categorie(categorie)
            if item:
                return {'items': [item.json() for item in item]}
            return {'message': 'Caterorie not found'},404   
