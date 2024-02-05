# Ejercicio 4
# Realizar una función que pida al usuario una palabra y muestre por pantalla si es un
# palíndromo o no.

def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")

    if palabra == palabra[::-1]:
        return True
    else:
        return False

entrada_usuario = input("Ingrese una palabra: ")

if palindromo(entrada_usuario):
    print( entrada_usuario + " es una palabra palíndromo.")
else:
    print(entrada_usuario + " no es una palabra palíndromo.")