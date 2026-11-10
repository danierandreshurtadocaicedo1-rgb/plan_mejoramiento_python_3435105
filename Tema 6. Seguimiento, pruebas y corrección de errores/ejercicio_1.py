# Ejercicio 01: Encontrar un error 
# Enunciado: Revisar el programa que calcula el promedio de dos notas, identificar el error logico y corregirlo.
# Entrada: nota1 = 4.0 y nota2 = 3.0
# Proceso: promedio = (nota1 + nota2) / 2
# Salida: Promedio esperado: 3.5

# Version con error logico:
# nota1 = 4.0
# nota2 = 3.0
# promedio = nota1 + nota2 / 2
# print("promedio:",promedio) da 5.5, porque la division se hace antes que la suma.

# Version corregida (con parentesis): los parentesis hacen que se haga primero la suma y asi lleve un orden logico matematico 
nota1 = 4.0
nota2 = 3.0
promedio = (nota1 + nota2) / 2
print("Promedio:", promedio)
