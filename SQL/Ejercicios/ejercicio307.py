import sqlite3  # Importamos la biblioteca "sqlite3" que darnos una API para poder usar bases de datos SQLite.

conexion=sqlite3.connect("database.db") # Crea una conexión con la base de datos llamada "database.db". Si no existe se creará automáticamente.
precio=float(input("Ingrese un precio:")) # Solicita que se ingrese un numero. El valor ingresado se convierte en un "float" y se almacena en la variable precio.
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
    # Ejecuta una consulta "select" para recuperar los nombres de los artículos que tienen un precio menor que el valor ingresado por el usuario.
filas=cursor.fetchall() # Recupera todas las filas del resultado de la consulta y las almacena en una lista llamada filas.
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()    # Cierra la conexión con la base de datos.

# Ingresando el numero del precio nos mostrara el registro con este mismo valor.