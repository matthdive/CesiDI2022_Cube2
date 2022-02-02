from sqlalchemy.sql import func
from . import db

class capteur(db.Model):
    id_capteur = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(150))


