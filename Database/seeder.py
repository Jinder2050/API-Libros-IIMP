import sqlite3 as sql


DB_PATH = "Database/libros.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE libros 
        (Titulo TEXT,
        Año INT,
        Autor TEXT
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