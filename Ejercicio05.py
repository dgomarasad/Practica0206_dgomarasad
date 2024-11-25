#Escribir un programa que cree un diccionario de traducción español-inglés.
#El usuario introducirá las palabras en español e inglés separadas por dos 
#puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el
#usuario introduzca la palabra “terminar”. El programa debe crear un 
#diccionario con las palabras y sus traducciones. Después pedirá una frase en
#español y utilizará el diccionario para traducirla palabra a palabra. Si una 
#palabra no está en el diccionario debe dejarla sin traducir.
# Crear un diccionario vacío
diccionario = {}
print("Introduce las palabras en formato <español>:<inglés>, separadas por comas. Escribe 'terminar' para finalizar.")
while True:
    entrada = input("Introduce una palabra en español y su traducción: ")
    
    if entrada.lower() == "terminar":
        break
    try:
        palabra, traduccion = entrada.split(":")
        diccionario[palabra.strip()] = traduccion.strip()
    except ValueError:
        print("Formato incorrecto. Asegúrate de usar <palabra>:<traducción>.")
frase = input("Introduce una frase en español para traducir: ")
palabras = frase.split()
traduccion = []
for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra))
print("Frase traducida:", " ".join(traduccion))


