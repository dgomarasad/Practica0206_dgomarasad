#Escribir un programa que guarde en una variable el diccionario 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y 
#muestre su símbolo o un mensaje de aviso si la divisa no está en el 
#diccionario.
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa_usuario = input("Introduce una divisa (Euro, Dollar,
                       "Yen): ").capitalize()
if divisa_usuario in divisas:
    print(f"El símbolo de {divisa_usuario} es {divisas[divisa_usuario]}")
else:
    print("La divisa no está en el diccionario.")




