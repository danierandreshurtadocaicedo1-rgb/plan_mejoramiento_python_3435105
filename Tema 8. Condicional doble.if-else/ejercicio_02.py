# Ejercicio 02: Par o impar
# Enunciado: Solicitar un número entero y determinar si es par o impar usando el operador módulo.
# Entrada: Un entero
# Proceso: numero % 2 == 0
# Salida: Par o impar

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
