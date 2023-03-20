from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Libros(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    year = db.Column(db.Integer)
    author = db.Column(db.String(200), nullable=False)

    def __str__(self) -> str:
        return f'\nTitulo: {self.title} -> year: {self.year} -> author: {self.author}\n.'
    
    def serialize(self):
        return {
            'rowid': self.rowid,
            'title': self.title,
            'year': self.year,
            'author': self.author
        }