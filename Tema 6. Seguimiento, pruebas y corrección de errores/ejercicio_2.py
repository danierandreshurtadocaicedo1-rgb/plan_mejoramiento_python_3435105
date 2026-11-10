# Ejercicio 02: Error de conversión
# Enunciado: Revisar un programa que usa input() para recibir dos números y los suma. Explicar qué ocurre y corregirlo.
# Entrada: Dos números (num1 y num2) entrados como texto (str)
# Proceso: Convertir con float() antes de sumar 
# Salida: Suma numérica

# Programa con error:
# num1 = input("Primer número: ")
# num2= input("Segundo número: ")
# suma = num1 + num2
# print("Suma:",suma)
# Qué ocurre: input() siempre guarda todo como texto (str). Si el se escribe 5 y 3, une los textos ("53") en vez de sumarlos.
#
# Programa corregido: se convierte cada dato a número antes de operar.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
suma = num1 + num2
print("Suma:", suma)