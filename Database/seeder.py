import sqlite3 as sql

#Las columnas de la tabla y las claves del json estaran en ingles por conflictos con caracteres especiales
DB_PATH = "Database/libros.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE libros 
        (title TEXT,
        year INT,
        author TEXT
        )"""
    )
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("INDICADOR DE COMPETITIVIDAD MINERA 2022",2022, "Gonzalo Tamayo - Socio Macroconsult"),
        ("ESPECIAL PERUMIN 35",2022,"IIMP"),
        ("COMPENDIO JUEVES MINERO 2022",2022,"IIMP"),
        ("Minería y Equilibrio Económico",2021,"Claudia Cooper Fort")
    ]
    cursor.executemany("""INSERT INTO libros VALUES (?, ?, ?)""",data)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    createDB()
    addValues()