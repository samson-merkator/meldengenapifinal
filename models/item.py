import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__='geometry_columns'

    id = db.Column(db.Integer, primary_key=True)
    idm = db.Column(db.String(80))
    date = db.Column(db.String(80))
    name = db.Column(db.String(80))
    telephone = db.Column(db.String(80))
    email = db.Column(db.String)
    categorie = db.Column(db.String)
    toelichting = db.Column(db.String)
    XCoordinaat = db.Column(db.Float)
    YCoordinaat = db.Column(db.Float)
    image = db.Column(db.String)

    def __init__(self, idm,date,name, telephone,email,categorie,toelichting,XCoordinaat,YCoordinaat,image):
        self.idm = idm
        self.date = date
        self.name = name
        self.telephone = telephone
        self.email = email
        self.categorie = categorie
        self.toelichting = toelichting 
        self.XCoordinaat = XCoordinaat
        self.YCoordinaat = YCoordinaat
        self.image = image



    def json(self):
        return{'id':self.idm,'date':self.date,'name':self.name, 'telephone':self.telephone,'email':self.email,'categorie':self.categorie,'toelichting':self.toelichting,'XCoordinaat':self.XCoordinaat,'YCoordinaat':self.YCoordinaat,'image':self.image}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def find_by_categorie(cls, categorie):
        return cls.query.filter_by(categorie=categorie)#SELECT * FROM items WHERE categorie=categorie LIMIT 1


  
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    #@classmethod
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



