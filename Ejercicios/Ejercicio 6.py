# Ejercicio 6
# Realizar una función que reciba una frase y devuelva un diccionario con las palabras
# que contiene y su longitud.

frase = "Hola buenas tardes"
diccionario: Map<> = {}
def diccionario(frase):
    lista = frase.split()
    for palabra in lista:
        diccionario[palabra] = len(palabra)

print(diccionario)
