# Ejercicio 03: Conversión de temperatura
# Enunciado: Solicitar una temperatura Celsius y convertirla a Fahrenheit con F = (C × 1.8) + 32.
# Entrada: Temperatura en °C
# Proceso: fahrenheit = (celsius * 1.8) + 32
# Salida: Temperatura en °F

temperatura = float(input(" ingrese la Temperatura en grados Celsius: "))
fahrenheit = (temperatura * 1.8) + 32
print(temperatura, "°C equivalen a", fahrenheit, "°F")