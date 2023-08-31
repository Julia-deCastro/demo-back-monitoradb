from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.String(50), nullable=True)
    modalidade = db.Column(db.String(50), nullable=True)
