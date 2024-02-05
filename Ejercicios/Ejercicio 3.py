# Ejercicio 3
# Basado en el ejercicio anterior realizar un programa que pregunte al usuario la nota
# que ha sacado en cada módulo y elimine de la lista los módulos aprobados. Al final el
# programa debe mostrar por pantalla los módulos que el usuario tiene que repetir.

modulos = ["Python", "SGE", "Programacion", "ERP", "Odoo"]
modulosRecuperar = []

for modulo in modulos:
    nota = int(input("Tu nota en " + modulo + ": "))
    if nota <= 5:
        modulosRecuperar.append(modulo)

for modulo in modulosRecuperar:
    print("Recuperar: " + modulo)