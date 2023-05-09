import sqlite3  # Se importa la biblioteca "sqlite"

db_filename = 'database.db' # Define el nombre del archivo de la base de datos

def display_table(conn):    # Define una función que muestra el contenido de la tabla "images"
    cursor = conn.cursor()
    cursor.execute('select name, size, date from images;')
    for name, size, date in cursor.fetchall():
        print(name, size, date)

# Abre una conexión con la base de datos SQLite y muestra el contenido de la tabla "images"
with sqlite3.connect(db_filename) as conn1: 
    print('Before changes:')
    display_table(conn1)

    # Inserta una nueva fila en la tabla "images"
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into images (name, size, date)
    values ('JournalDev.png', 2000, '2020-02-20');
    """)

    # Muestra el contenido de la tabla "images" después de la inserción.
    print('\nAfter changes in conn1:')
    display_table(conn1)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    # Commit from the first connection
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        display_table(conn3)
        
    # Inserta una nueva fila en la tabla "images"
    cursor1.execute("""
    insert into images (name, size, date)
    values ('Hello.png', 200, '2020-01-18');
    """)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2) 

    # Revert to changes before conn1's commit
    conn1.rollback()    # Revoca los cambios en la primera conexión
    # Muestra el contenido de la tabla "images" después de revocar los cambios en la primera conexión
    print('\nAfter connection 1 rollback:')
    with sqlite3.connect(db_filename) as conn4:
        display_table(conn4)
