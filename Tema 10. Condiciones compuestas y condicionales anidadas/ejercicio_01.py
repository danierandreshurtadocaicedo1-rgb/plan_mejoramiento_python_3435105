# Ejercicio 01: Acceso a una plataforma
# Enunciado: Solicitar usuario y si la contraseña es correcta. Si el usuario es 'aprendiz' y la contraseña es correcta, permitir el acceso.
# Entrada: Usuario y si la contraseña es correcta  la contraseña es correcta (si/no)
# Proceso: if anidado
# Salida: Acceso permitido o rechazado

usuario = input("ingrese el nombre de Usuario: ")
clave_correcta = input("¿La contraseña es correcta? (si/no): ").lower() == "si"
if usuario == "aprendiz":
    if clave_correcta:
        print("Acceso permitido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no reconocido")
