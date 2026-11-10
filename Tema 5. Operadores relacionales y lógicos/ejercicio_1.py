# Ejercicio 01: Evaluar condiciones (resuelto en la guía)
# Enunciado: Solicitar la edad y mostrar, con una expresión lógica, si es mayor o igual a 18 (sin usar if).
# Entrada: Edad
# Proceso: mayor_edad = edad >= 18
# Salida: True o False

edad = int(input("Ingrese la edad: "))
mayor_edad = edad >= 18
print("¿Tiene 18 años o más?", mayor_edad)