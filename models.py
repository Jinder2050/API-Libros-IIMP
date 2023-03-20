from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Libros(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    year = db.Column(db.Integer)
    author = db.Column(db.String(200), nullable=False)
    languaje = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self,title,year,author,languaje,status,url) -> None:
        super().__init__()
        self.title = title
        self.year = year
        self.author = author
        self.languaje = languaje
        self.status = status
        self.url = url

    def __str__(self) -> str:
        return f'\nTitulo: {self.title} -> year: {self.year} -> author: {self.author} -> languaje: {self.languaje} -> status: {self.status} -> url: {self.url}\n.'
    
    def serialize(self) -> dict:
        """
        Esta funcion retorna un diccionario, se usará con la funcion `jsonify`
        """
        return {
            'rowid': self.rowid,
            'title': self.title,
            'year': self.year,
            'author': self.author,
            'languaje': self.languaje,
            'status': self.status,
            'url': self.url
        }