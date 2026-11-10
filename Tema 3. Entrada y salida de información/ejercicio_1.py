# Ejercicio 01: Costo de entradas 
# Enunciado: Solicitar el nombre de un evento, el precio de la entrada y la cantidad comprada. Calcular y presentar el costo total.
# Entrada: Evento, precio y cantidad
# Proceso: total = precio * cantidad
# Salida: Evento, cantidad y costo total

evento = input("Nombre del evento: ")
precio = float(input("Precio de la entrada: "))
cantidad = int(input("Cantidad de entradas: "))
total = precio * cantidad
print("Evento:", evento)
print("Cantidad:", cantidad)
print("Costo total:", total)