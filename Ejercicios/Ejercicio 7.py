# Ejercicio 7
# Realizar  una  función  que  pida  la  anchura  de  un  triángulo  y
# lo  dibuje  con  caracteres producto (*)

def dibujarTriangulo(altura):
    triangulo=""

    for i in range(1,altura+1):
        nivel = "*" * i
        print(nivel)

    for i in range(1, altura+1):
        nivel = "*" * (altura - i)
        print(nivel)


print(dibujarTriangulo(4))