# Ejercicio 02: Rango válido
# Enunciado: Solicitar un número y determinar si está entre 10 y 50 inclusive utilizando and.
# Entrada: Un número
# Proceso: if numero >= 10 and numero <= 50
# Salida: Dentro o fuera del rango

numero = float(input("Ingrese un número: "))
if numero >= 10 and numero <= 50:
    print("El número está dentro del rango (10 a 50)")
else:
    print("El número está fuera del rango")
