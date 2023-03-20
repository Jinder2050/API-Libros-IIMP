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
        author TEXT,
        languaje TEXT,
        status TEXT,
        url TEXT
        )"""
    )
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("Indicador de competitividad minera",2022, "Gonzalo Tamayo - Socio Macroconsult", 'Español','Publicado','https://iimp.org.pe/asociado/memorias/2022/2022_09_28_Presentacion_PERUMIN_35.pdf'),
        ("Especial perumin 35",2022,"IIMP", 'Español','Publicado','https://perumin.com/perumin35/especial/ppt/ESPECIAL%20PERUMIN%2035.pdf'),
        ("Compendio jueves minero 2022",2022,"IIMP",'Español','Publicado','https://iimp.org.pe/jueves_minero/compendio/2022/pdf/Especial.pdf'),
        ("Minería y Equilibrio Económico",2021,"Claudia Cooper Fort", 'Español','Publicado','https://iimp.org.pe/archivos/publicaciones/LIBRO-MINERIA-Y-EQUILIBRIO-ECONOMICO.pdf'),
        ('Estudio de proveedores mineros del Peru',2021,'SAMMI - Clúster Minero Andino','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20211124-123006-1fa1.pdf'),
        ('Estudio: Beneficios de la Minería en el Perú',2021,'Centro para la Competitividad y el Desarrollo','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20210326-023338-2454.pdf'),
        ('Estudio: Oportunidad de Desarrollo Frente a la Crisis Nacional',2021,'PERUMIN','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20210406-071159-1db4.pdf'),
        ('Encuesta Minería 2021: Alerta máxima ante el riesgo político',2021,'BNamericas','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20211228-062736-1794.pdf'),
        ('Mining Survey 2021: High Alert as Political Risk Takes Center Stage',2021,'BNamericas','Inglés','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20211228-063132-113e.pdf'),
        ('Especial Jueves Mineros Virtuales 2021',2021,'IIMP','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20220309-035638-1387.pdf'),
        ('Especial Rumbo a PERUMIN',2021,'IIMP','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20220309-035748-24d3.pdf'),
        ('Minería del Bicentenario',2021,'IIMP','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20220309-035841-bf5.pdf'),
        ('Especial I Congreso de Competitividad Minera y Sostenibilidad social',2021,'IIMP','Español','Publicado','https://iimp.org.pe/archivos/publicaciones/a621-20220309-040014-630.pdf'),
        ('Memoria Institucional 2021',2021,'IIMP','Español','Publicado','https://iimp.org.pe/asociado/memorias/2021/')
    ]
    cursor.executemany("""INSERT INTO libros VALUES (?, ?, ?, ?, ?, ?)""",data)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    createDB()
    addValues()