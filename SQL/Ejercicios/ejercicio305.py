import sqlite3  # Importamos la biblioteca "sqlite3" que darnos una API para poder usar bases de datos SQLite.

conexion=sqlite3.connect("database.db") # Crea una conexión con la base de datos llamada "database.db". Si no existe se creará automáticamente.
cursor=conexion.execute("select codigo,descripcion,precio from articulos")
    # Se Ejecuta una consulta "select" para recuperar los datos de la tabla articulos(codigo,descripcion,precio).
    # Todo esto pasa dentro de la variable "cursor"
for fila in cursor: #   Itera sobre las filas devueltas por el objeto de cursor.
    print(fila)     #   imprime cada fila en la consola.
conexion.close()    # Cierra la conexión con la base de datos.

# Este comando nos muestra en una lista lo que tenemos dentro de nuestra bbdd.