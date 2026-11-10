# Ejercicio 02: Clasificación de temperatura
# Enunciado: Clasificar la temperatura: fría (<15), templada (15 a 25 inclusive) y caliente (>25).
# Entrada: Temperatura
# Proceso: if / elif / else
# Salida: Fría, templada o caliente

temperatura = float(input("Ingrese la temperatura: "))
if temperatura < 15:
    print("Temperatura fría")
elif temperatura <= 25:
    print("Temperatura templada")
else:
    print("Temperatura caliente")
# tambien se puede con el operador logico and, pero no es necesario en este caso ya que el elif 
# ya cubre el rango de 15 a 25.
# temperatura = float(input("Ingrese la temperatura: "))
# if temperatura < 15:
#     print("Temperatura fría")
# elif temperatura >= 15 and temperatura <= 25:
#     print("Temperatura templada")
# else:
#     print("Temperatura caliente")