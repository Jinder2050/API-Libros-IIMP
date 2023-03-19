from flask import Flask
from models import db, Libros

# file_path = os.path.abspath(os.getcwd())+"\libros.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///E:\PROGRAMACION PYTHON\API\Database\libros.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route('/')
def home():
    return '<h1>Hola</h1>'


@app.route("/api/libros")
def getLibros():
    libros = Libros.query.all()
    print(libros)
    return '<h1>Pass</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=4000)