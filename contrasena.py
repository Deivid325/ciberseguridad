from utilidades import comprobar_numero

contrasena = "Hola1234"

def comprobar_longitud(contrasena):
    if len(contrasena) >= 8:
        return True
    else:
        return False

print("Contraseña:", contrasena)
print("Longitud válida:", comprobar_longitud(contrasena))

print("Prueba corta:", comprobar_longitud("Hola12"))
print("Prueba larga:", comprobar_longitud("Hola1234"))

print("Tiene números:", comprobar_numero(contrasena))

print("Prueba con números:", comprobar_numero("Hola123"))
print("Prueba sin números:", comprobar_numero("HolaMundo"))