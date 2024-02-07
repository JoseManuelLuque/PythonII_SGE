# Ejercicio 6
# Realizar una función que reciba una frase y devuelva un diccionario con las palabras
# que contiene y su longitud.



def diccionario(frase):
    diccionario = {}

    lista = frase.split()
    for elemento in lista:
        if elemento == " ":
            lista.remove(elemento)
    for palabra in lista:
        diccionario[palabra] = len(palabra)

    return diccionario


frase = "Hola buenas tardes"
print(diccionario(frase))