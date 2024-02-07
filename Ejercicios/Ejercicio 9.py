# Ejercicio 9
# Realizar  un  programa  que  guarde  los  números  que  el  usuario  vaya
# introduciendo;  elcriterio de finalización es cuando introduzca algo que
# no sea un número. Una vez que haya  terminado,  el  usuario  debe  indicar
# un  número  que  haya  introducido  y  el ordenador deberá decirle el puesto
# en el que lo metió

def guardaNumeros():
    numeros = []
    while True:
        try:
            num = input("Introduce un número (o introduce cualquier otra cosa para finalizar): ")
            num = float(num)
            numeros.append(num)
        except ValueError:
            break
    return numeros

def encontrarPuesto(numero, numeros):
    if numero in numeros:
        puesto = numeros.index(numero) + 1
        return puesto
    else:
        return None


numeros_guardados = guardaNumeros()

numero_buscado = float(input("Introduce un número que hayas introducido anteriormente: "))

puesto = encontrarPuesto(numero_buscado, numeros_guardados)

if puesto is not None:
    print(f"El número {numero_buscado} fue introducido en el puesto {puesto}.")
else:
    print("El número no fue encontrado en la lista de números introducidos.")



