#Escribir un programa que acceda al fichero de internet mediante la ur
#indicada y muestre por pantalla el número de palabras que contiene.
import requests

# Descargar el archivo desde la URL
url = "http://textfiles.com/adventure/aencounter.txt"
respuesta = requests.get(url)

# Obtener el contenido del archivo como texto
texto = respuesta.text

# Contar el número de palabras
palabras = texto.split()

# Mostrar el número de palabras
print(f"El número de palabras en el archivo es: {len(palabras)}")



