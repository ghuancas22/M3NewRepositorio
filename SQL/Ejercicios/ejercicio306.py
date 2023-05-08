import sqlite3  # Importamos la biblioteca "sqlite3" que darnos una API para poder usar bases de datos SQLite.

conexion=sqlite3.connect("database.db") # Crea una conexión con la base de datos llamada "database.db". Si no existe se creará automáticamente.
codigo=int(input("Ingrese el código de un artículo:"))
# Solicita que se ingrese el código de un artículo este mismo se convierte en in "integer" y se almacena en la variable "codigo".
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))
# Se hace un "select" para recuperar los datos del artículo especificado por el usuario. Donde se muestra el valor igualado al ingresado.
fila=cursor.fetchone() # Recupera la primera fila del resultado de la consulta. Si hay varias filas "fetchone()" solo recuperará la primera.
if fila!=None:  # Revisa si se encontró un registro que coincida con el código proporcionado. 
    print(fila) # Se muestra si se logro encontrar
else:
    print("No existe un artículo con dicho código.")    # Si en caso no existe se manda un mensaje.
conexion.close()    # Cierra la conexión con la base de datos.

# Este codigo sirve para poder buscar o revisar lo que tenemos dentro de nuestra base de datos.