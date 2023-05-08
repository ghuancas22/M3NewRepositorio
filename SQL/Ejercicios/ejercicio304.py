import sqlite3 #Importamos la biblioteca "sqlite3" que darnos una API para poder usar bases de datos SQLite.

conexion=sqlite3.connect("database.db") # Crea una conexión con la base de datos llamada "database.db". Si no existe se creará automáticamente.
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
    # Inserta un registro en la tabla articulos. Se usa "insert into articulos(descripcion,precio) values (?,?)" para definir.   
    # Se llena con los valores "("naranjas", 23.50)".
conexion.commit()   # Confirma los cambios realizados.
conexion.close()    # Cierra la conexión con la base de datos.

#Estos comandos sirven para poder agregar valores a nuestro registro de la bbdd.