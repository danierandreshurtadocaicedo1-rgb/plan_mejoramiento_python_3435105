# Ejercicio 03: Variable mal escrita
# Enunciado: Programa que calcule el área de un rectángulo. Introducir un nombre de variable distinto en la salida, ejecutar y corregir.
# Entrada: Base y altura
# Proceso: area = base * altura
# Salida: Área del rectángulo

# Versión con error (nombre distinto en la salida):
# base = float(input("Ingrese la base: "))
# altura = float(input("Ingrese la altura: "))
# area = base * altura
# print("Área:", aera)
# Al ejecutarla Python muestra: NameError: name 'aera' is not defined
# Corrección: usar exactamente el mismo nombre de la variable, "area".

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = base * altura
print("Área:", area)