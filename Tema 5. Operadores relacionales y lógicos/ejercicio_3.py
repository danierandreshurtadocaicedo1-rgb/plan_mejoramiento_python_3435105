# Ejercicio 03: Rango de edad
# Enunciado: Solicitar una edad y construir una expresión lógica True cuando esté entre 18 y 28 años (límites incluidos).
# Entrada: Edad
# Proceso: en_rango = edad >= 18 and edad <= 28
# Salida: True o False


edad = int(input("Ingrese la edad: "))
en_rango = edad >= 18 and edad <= 28
print("¿Está entre 18 y 28 años?", en_rango)