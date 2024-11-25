#Escribir un programa que permita gestionar la base de datos de alumnado
#de un classroom. Los alumnos y alumnas se guardarán en una lista que almacena
#un diccionario para cada alumno/a en el que la clave de cada alumno/a será su
#NIF, y el valor será otro diccionario con los datos del alumno/a (nombre,
#apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True
#si ha aprobado el módulo. El programa debe preguntar al usuario por una opción
#del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar 
#alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:
#Preguntar los datos del alumno/a, crear un diccionario con los 
#datos y añadirloa la base de datos.
#Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
#Preguntar por el NIF del alumno/a y mostrar sus datos.
#Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
#Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
#Termina el programa.
# Base de datos de alumnos (diccionario con NIF como clave)
alumnos = {}
def añadir_alumno():
    nif = input("Introduce el NIF del alumno: ")
    nombre = input("Introduce el nombre del alumno: ")
    apellidos = input("Introduce los apellidos del alumno: ")
    telefono = input("Introduce el telefono del alumno: ")
    correo = input("Introduce el correo electrónico del alumno: ")
    aprobado = input("¿Ha aprobado el modulo? (si/no): ").lower() == "si"
    alumnos[nif] = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "aprobado": aprobado
    }
    print(f"Alumno {nombre} {apellidos} añadido.")

