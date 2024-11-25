#Escribir un programa que guarde en un diccionario los precios de los
#artículos de la tabla, pregunte al usuario por un artículo, un número de 
#unidades y muestre por pantalla el precio de esa cantidad de producto. 
#Si el producto no está en el diccionario debe mostrar un mensaje informando
# de ello.
prdcts = {'Pan':1.4,'Huevos':2.3,'Cebolla':0.85,'Aceite':4.35}
productos = input('Que producto quieres de la lista: ').capitalize()
unidades = float(input("Dime cuantas unidades quieres del producto: "))
if productos in prdcts:
    precio = int(prdcts[productos] * unidades)
    print(f"El precio de {productos} es de {precio :.2f}€ ")
else:
    print("El producto no está disponible")
