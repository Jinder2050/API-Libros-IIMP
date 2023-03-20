from flask import Flask, jsonify, request, render_template
from models import db, Libros
from logging import exception
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///E:\PROGRAMACION PYTHON\API\Database\libros.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#Primera plantilla
@app.route('/')
def home():
    '''
    Esta funcion devuelve el formulario de entrada de datos
    '''
    return render_template('index.html')

#Segunda plantilla
@app.route('/searchtitle', methods=['GET'])
def searchtitle():
    '''
    Esta funcion devuelve el buscador de libro por el titulo
    '''
    return render_template('searchtitle.html')

#Las columnas de la tabla y las claves del json estaran en ingles por conflictos con caracteres especiales
@app.route("/api/libros", methods=['GET'])
def getLibros():
    try:
        libros = Libros.query.all()
        toReturn = [libro.serialize() for libro in libros]
        return jsonify(toReturn), 200
    except Exception as e:
        print(f"--> [SERVER] : ERROR: {e}")
        return jsonify({'msg': 'Ocurrio un error'}), 500


#Esta funcion filtra el libro por el titulo
@app.route('/api/libro', methods=['GET']) #----> ruta
def getLibroByTitle():
    try:
        tituloLibro = request.args['title']
        libro = Libros.query.filter_by(title=tituloLibro).first()
        if not libro:
            return jsonify({'msg': 'Este libro no existe'}), 200
        else:
            return jsonify(libro.serialize()), 200
    except Exception as e:
        print(f"--> [SERVER] : ERROR: {e}")
        return jsonify({'msg': 'Ocurrio un error'}), 500


#Esta funcion filtra el libro por muchos parametros
@app.route('/api/filtrarlibro', methods=['GET']) # ----> Ruta
def getLibro():
    try:
        fields = {}
        if 'title' in request.args:
            fields['title'] = request.args['title']
            
        if 'author' in request.args:
            fields['author'] = request.args['author']

        if 'year' in request.args:
            fields['year'] = request.args['year']

        if 'languaje' in request.args:
            fields['languaje'] = request.args['languaje']

        if 'status' in request.args:
            fields['status'] = request.args['status']

        if 'url' in request.args:
            fields['url'] = request.args['url']

        libro = Libros.query.filter_by(**fields).first()

        if not libro:
            return jsonify({'msg': 'Este libro no existe'}), 200
        else:
            return jsonify(libro.serialize()), 200
    except Exception:
        exception('--> [SERVER]: Error')
        return jsonify({'msg': 'Ocurrio un error'}), 500


@app.route('/api/addlibro', methods=['POST'])
def addlibro():
    try:
        title = request.form['title']
        year = request.form['year']
        author = request.form['author']
        languaje = request.form['languaje']
        status = request.form['status']
        url = request.form['url']

        libro = Libros(title, int(year), author, languaje, status, url)
        db.session.add(libro)
        db.session.commit()

        return jsonify(libro.serialize()), 200
    except Exception:
        exception('\n -->[SERVER]: Error en /api/addlibro, log:\n')
        return jsonify({'msg':'Ocurrio un error'}), 500


@app.route('/api/searchtitle', methods=['POST']) #----> ruta
def searchTitleForm():
    try:
        tituloLibro = request.form['title']
        libro = Libros.query.filter(Libros.title.like(f'%{tituloLibro}%')).first()
        if not libro:
            return jsonify({'msg': 'Este libro no existe'}), 200
        else:
            return jsonify(libro.serialize()), 200
    except Exception:
        exception('--> [SERVER]: Error en la ruta /api/searchtitle --> ')
        return jsonify({'msg': 'Ocurrio un error'}), 500


if __name__ == '__main__':  
    app.run(debug=True, port=4000),500