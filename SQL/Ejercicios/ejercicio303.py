import sqlite3 #Importamos la biblioteca "sqlite3" que darnos una API para poder usar bases de datos SQLite.

conexion=sqlite3.connect("database.db") # Crea una conexión con la base de datos llamada "database.db". Si no existe se creará automáticamente.
try: 
    conexion.execute("""create table articulos (                        
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    # Crea una tabla llamada articulos con tres columnas: codigo, descripcion y precio.
    # La columna "codigo" se define como una clave principal con "primary key" y se incrementa automáticamente con "autoincrement".
    
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:   #Se utiliza "try-except" para controlar el "OperationalError" que puede ocurrir si la tabla ya existe.
    #Si la tabla existe se muestra un "Print" que confirma que la tabla ya esta creada.
    print("La tabla articulos ya existe")                    
conexion.close() # Cierra la conexión con la base de datos. 

