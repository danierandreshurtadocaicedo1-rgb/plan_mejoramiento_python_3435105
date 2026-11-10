#Ejercicio 1 resuelto: costo de una compra
#Enunciado: solicitar el precio unitario de un producto y la cantidad comprada. Calcular y mostrar el costo total.
# Entrada: precio unitario y cantidad
#proceso: total = precio por cantidad
# salida: costo total 


precio =float(input("ingrese el precio unitario: "))
cantidad = int(input("ingrese la cantidad comprada: "))
total = precio * cantidad
print("el costo total de la compra es :", total)
