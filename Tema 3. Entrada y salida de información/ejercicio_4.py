# Ejercicio 04: Factura de un pedido
# Enunciado: Solicitar producto, precio unitario y cantidad. Calcular el subtotal y mostrar una factura sencilla.
# Entrada: Producto, precio unitario y cantidad
# Proceso: subtotal = precio * cantidad
# Salida: Factura sencilla

producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
subtotal = precio * cantidad
print("------ FACTURA ------")
print("Producto:", producto)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Subtotal:", subtotal)