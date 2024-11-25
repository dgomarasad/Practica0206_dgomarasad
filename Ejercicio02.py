#Escribir un programa que pregunte al usuario su nombre, edad, dirección y
# teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
#el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>”.
nom = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
telefono = input("Dime tu telefono: ")
direccion = input("Dime tu direccion: ")
Datos = {"Nombre":nom,"Edad":edad,"Telefono":telefono,"Direccion":direccion}
print(f"{nom} tiene {edad}años,vive en {direccion}y su numero de telefono es {telefono})

