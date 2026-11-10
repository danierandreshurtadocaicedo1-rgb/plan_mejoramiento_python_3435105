# Ejercicio 04: Costo de alojamiento
# Enunciado: Solicitar la tarifa por noche y el número de noches. Calcular el costo total.
# Entrada: Tarifa por noche y número de noches
# Proceso: total = tarifa * noches
# Salida: Costo total del alojamiento

tarifa = float(input("Tarifa por noche: "))
noches = int(input("Número de noches: "))
total = tarifa * noches
print("El costo total del alojamiento es:", total)