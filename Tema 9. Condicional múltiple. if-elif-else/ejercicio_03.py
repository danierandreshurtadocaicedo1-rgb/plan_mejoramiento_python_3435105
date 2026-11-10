# Ejercicio 03: Menú de operaciones
# Enunciado: Solicitar un número entre 1 y 3 y mostrar una opción distinta para cada valor; si no coincide, Opción no válida.
# Entrada: Número de opción
# Proceso: if / elif / else
# Salida: Opción seleccionada

opcion = int(input("Elija una opción (1, 2 o 3): "))
if opcion == 1:
    print("Opción 1: Consultar saldo")
elif opcion == 2:
    print("Opción 2: Realizar un depósito")
elif opcion == 3:
    print("Opción 3: Salir")
else:
    print("Opción no válida")
