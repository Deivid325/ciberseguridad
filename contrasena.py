from utilidades import comprobar_numero

contrasena = "Hola1234"


def comprobar_longitud(contrasena):
    if len(contrasena) >= 12:
        return True
    else:
        return False


def comprobar_mayuscula(contrasena):
    for caracter in contrasena:
        if caracter.isupper():
            return True
    return False


print("Contraseña:", contrasena)
print("Tiene mayúsculas:", comprobar_mayuscula(contrasena))
print("Prueba con mayúsculas:", comprobar_mayuscula("Hola1234"))
print("Prueba sin mayúsculas:", comprobar_mayuscula("hola1234"))

print("Longitud válida:", comprobar_longitud(contrasena))
print("Prueba corta:", comprobar_longitud("Hola12"))
print("Prueba larga:", comprobar_longitud("Hola1234"))

print("Tiene números:", comprobar_numero(contrasena))

print("Prueba con números:", comprobar_numero("Hola123"))
print("Prueba sin números:", comprobar_numero("HolaMundo"))