# Ejercicio 1
# Realizar un programa que guarde la cadena de caracteres contraseña en una variable
# y pregunte al usuario por la contraseña hasta que coincida con la contraseña
# guardada.


while True:
    opcion = int(input("1. Registrar contraseña\n2. Iniciar Sesion\n3. Cerrar\n\n"))

    if opcion == 1:
        contrasenia = input("Ingrese la nueva contraseña: ")
    if opcion == 2:
        contraseniaComprobar = input("Ingrese la contraseña para iniciar sesion: ")
        if contrasenia == contraseniaComprobar:
            print("Sesión iniciada")
        else:
            while contrasenia != contraseniaComprobar:
                contraseniaComprobar = input("Contraseña incorrecta, vuelva a introducirla: ")
            print("Sesión iniciada")

    if opcion == 3:
        break