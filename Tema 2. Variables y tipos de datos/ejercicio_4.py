# Ejercicio 04: Registro de ventas
# Enunciado: Solicitar nombre del vendedor, cantidad de productos vendidos y valor total de las ventas. Presentar un resumen.
# Entrada: Vendedor (str), cantidad (int), valor total (float)
# Proceso: Almacenar cada dato en una variable
# Salida: Resumen de ventas

vendedor = input("Nombre del vendedor: ")
cantidad = int(input("Cantidad de productos vendidos: "))
valor_total = float(input("Valor total de las ventas: "))
print("--- Resumen de ventas ---")
print("Vendedor:", vendedor)
print("Productos vendidos:", cantidad)
print("Valor total:", valor_total)