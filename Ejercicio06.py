#Escribir un programa para gestionar un listín telefónico con los nombres y
#los teléfonos de los clientes de una empresa. El programa debe  incorporar
#funciones para crear el fichero con el listín si no existe, para consultar 
#el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar
#el teléfono de un cliente. El listín debe estar guardado en el fichero de 
#texto listin.txt donde el nombre del cliente y su teléfono deben aparecer
#separados por comas y cada cliente en una línea distinta.
# Función para crear el archivo si no existe
def crear_listin():
    try:
        with open("listin.txt", "x"):
            print("El archivo 'listin.txt' ha sido creado.")
    except FileExistsError:
        print("El archivo 'listin.txt' ya existe.")
def consultar_cliente(nombre):
    try:
        with open("listin.txt", "r") as archivo:
            for linea in archivo:
                cliente, telefono = linea.strip().split(",")
                if cliente.lower() == nombre.lower():
                    print(f"El teléfono de {nombre} es {telefono}.")
                    return
            print(f"No se encontró a {nombre} en el listín.")
    except FileNotFoundError:
        print("El archivo 'listin.txt' no existe. Crea el archivo primero.")
def añadir_cliente(nombre, telefono):
    with open("listin.txt", "a") as archivo:
        archivo.write(f"{nombre},{telefono}\n")
    print(f"{nombre} ha sido añadido al listín.")
def eliminar_cliente(nombre):
    try:
        with open("listin.txt", "r") as archivo:
            lineas = archivo.readlines()
        with open("listin.txt", "w") as archivo:
            encontrado = False
            for linea in lineas:
                if not linea.startswith(nombre + ","):
                    archivo.write(linea)
                else:
                    encontrado = True
            if encontrado:
                print(f"{nombre} ha sido eliminado del listín.")
            else:
                print(f"No se encontró a {nombre} en el listín.")
    except FileNotFoundError:
        print("El archivo 'listin.txt' no existe. Crea el archivo primero.")
def menu():
    while True:
        print("\nGestión del Listín Telefónico")
        print("1. Crear listin")
        print("2. Consultar telefono")
        print("3. Añadir cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            crear_listin()
        elif opcion == "2":
            nombre = input("Introduce el nombre del cliente: ")
            consultar_cliente(nombre)
        elif opcion == "3":
            nombre = input("Introduce el nombre del cliente: ")
            telefono = input("Introduce el teléfono del cliente: ")
            añadir_cliente(nombre, telefono)
        elif opcion == "4":
            nombre = input("Introduce el nombre del cliente a eliminar: ")
            eliminar_cliente(nombre)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")


menu()
