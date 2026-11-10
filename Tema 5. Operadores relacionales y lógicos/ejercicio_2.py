# Ejercicio 02: Comparación de dos números
# Enunciado: Solicitar dos números y mostrar los resultados de las comparaciones: igual, diferente, mayor y menor.
# Entrada: Dos números (num1 y num2)
# Proceso: Comparar con ==, !=, > y <
# Salida: resultados de las comparaciones 


num1 = float(input("ingrese el Primer número: "))
num2 = float(input("ingrese el Segundo número: "))
es_igual = (num1 == num2)
es_diferente = (num1 != num2)
es_mayor = (num1 > num2)
es_menor = (num1 < num2)
print("¿Son iguales?", es_igual)
print("¿Son diferentes?", es_diferente)
print("¿El primero es mayor?", es_mayor)
print("¿El primero es menor?", es_menor)