import sqlite3  # Se importa la biblioteca "sqlite"

db_file = 'database.db'  # Define el nombre del archivo de la base de datos

with sqlite3.connect(db_file) as conn:  # Establece una conexión con db_file
    cursor = conn.cursor()  # Crea un objeto cursor que se utilizará para realizar consultas.
    cursor.execute("""
                   select * from images
                   """)
    # Ejecuta una consulta "SELECT" para seleccionar todas las columnas y filas de la tabla
    for row in cursor.fetchall():
        name, size, date = row
        # almacena las columnas 'name', 'size' y 'date' de la fila actual en variables separadas para su uso.
        print(f'{name} {size} {date}') # A continuacion se imprime os valores dados.