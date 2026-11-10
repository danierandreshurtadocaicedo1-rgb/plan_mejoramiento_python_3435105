# Ejercicio 04: Tarifa de transporte
# Enunciado: Solicitar la edad. Tarifa infantil (<12), juvenil (12 hasta antes de 18) y general (>= 18).
# Entrada: Edad
# Proceso: if / elif / else
# Salida: Tarifa aplicable

edad = int(input("Ingrese la edad: "))
if edad < 12:
    print("Tarifa infantil")
elif edad < 18:
    print("Tarifa juvenil")
else:
    print("Tarifa general")


# edad = int(input("Ingrese la edad: "))
# if edad < 12:
#     print("Tarifa infantil")
# elif edad >= 12 and edad < 18:
#     print("Tarifa juvenil")
# else:
#     print("Tarifa general")