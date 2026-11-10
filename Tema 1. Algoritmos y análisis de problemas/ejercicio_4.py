# Ejercicio 4. Aplicación — Consumo de combustible
# Enunciado:Solicite la distancia recorrida y los litros de combustible consumidos. Calcule los kilómetros por litro
# Suponga que los litros son mayores que cero.
# Entrada: distancia (km) y litros consumidos 
# proceso: consumo = distancia / litros 
# salida: kilómetros por litro 
distancia = float(input("ingrese la distancia recorrida (km):"))
litros = float(input("litros de combustible consumidos:"))
consumo = distancia / litros
print("el consumo del vehiculo es de:",consumo,"km/l")