# Ejercicio 04: Resultado incorrecto
# Enunciado: Un programa calcula el total de una compra sumando precio unitario y cantidad. Identificar por qué es incorrecto y corregirlo.
# Entrada: Precio unitario y cantidad
# Proceso: total = precio * cantidad
# Salida: Costo total

# Versión con error (operación matemática incorrecta):
# precio = float(input("Ingrese el precio unitario: "))
# cantidad = int(input("Ingrese la cantidad: "))
# total = precio + cantidad
# Al ejecutarla, con precio 2500 y cantidad 4 da 2504 porque usa una suma en lugar de una multiplicación.
# Corrección: cambiar el operador de suma (+) por el de multiplicación (*).

precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))
total = precio * cantidad
print("Costo total:", total)