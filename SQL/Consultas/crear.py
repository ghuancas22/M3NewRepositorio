import sqlite3  # Se importa la biblioteca "sqlite"
import os       # Se importa la biblioteca "os"

def check_db(filename):
    return os.path.exists(filename)

# Define una función "check_db" que toma el nombre del archivo de la base de datos
# devuelve True si el archivo existe en el sistema, y False en caso contrario.

db_file = 'database.db'
schema_file = 'schema.sql'
# Asigna los nombres de la base de datos y del archivo de esquema a las variables db_file y schema_file.

if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)
# Verifica si la base de datos ya existe en el sistema llamando a la función "check_db".
# Si la base de datos existe, imprime un mensaje y sale del programa con "exit(0)"".

with open(schema_file, 'r') as rf: # Abre el archivo de esquema en modo de lectura y lo lee en una variable llamada "schema"
    # Read the schema from the file
    schema = rf.read()

with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
    # Execute the SQL query to create the table
    conn.executescript(schema)
    print('Created the Table! Now inserting')
    conn.executescript("""
                       insert into images (name, size, date)
                       values
                       ('sample.png', 100, '2019-10-10'),
                       ('ask_python.png', 450, '2019-05-02'),
                       ('class_room.jpeg', 1200, '2018-04-07');
                       """)
    print('Inserted values into the table!')
print('Closed the connection!')
