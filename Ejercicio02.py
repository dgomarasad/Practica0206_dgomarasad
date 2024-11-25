#Escribir un programa que pregunte al usuario su nombre, edad, dirección y
# teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
#el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>”.
# Crear un diccionario para almacenar los datos
datos = {}
datos["nombre"] = input("Introduce tu nombre: ")
datos["edad"] = input("Introduce tu edad: ")
datos["dirección"] = input("Introduce tu dirección: ")
datos["teléfono"] = input("Introduce tu número de teléfono: ")

print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['dirección']} y su número de teléfono es {datos['teléfono']}.")


