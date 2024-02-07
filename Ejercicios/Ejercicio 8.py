# Ejercicio 8
# Realizar  un  programa  que  cree  una  lista  de  palabras
# (que  puede  ser  vacía).  El programa debe  pedir el número de palabras
# que van a estar en la lista y luego solicitar ese número de palabras para
# crear la lista. Por último, el programa tiene que escribir la lista.

def listaPalabras():
    numeroPalabras = int(input("Ingrese el número de palabras que desea agregar a la lista: "))
    lista_palabras = []

    for i in range(numeroPalabras):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        lista_palabras.append(palabra)

    return lista_palabras

print("La lista de palabras creada es:", listaPalabras())
