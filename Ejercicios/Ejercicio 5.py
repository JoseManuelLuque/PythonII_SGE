# Ejercicio 5
# Realizar un programa que guarde en un diccionario los precios de las frutas de la
# tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
# precio de la fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
# informando de ello.
# Fruta Precio
# Plátano 1.35
# Manzana 0.80
# Pera 0.85
# Naranja 0.70

frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

print("Lista de frutas:")
for fruta in frutas: print(fruta)
print("")

fruta = input("Por favor ingrese una fruta de la lista de frutas: ")

while fruta not in frutas:
    fruta = input("No existe en la lista esa fruta, por favor ingrese una: ")

kilos = input("Por favor ingrese el numero de kilos que quiere: ")

precio = frutas[fruta] * float(kilos)

print("Precio Total: " + str(precio) + " €")