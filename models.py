from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Libros(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(200), unique=True, nullable=False)
    Año = db.Column(db.Integer)
    Autor = db.Column(db.String(200), nullable=False)
