# Ejercicio 03: Repartición de elementos
# Enunciado: Solicitar la cantidad de elementos y el número de personas (> 0). Calcular cuántos recibe cada una y cuántos sobran.
# Entrada: Cantidad de elementos y número de personas
# Proceso: cada_uno = elementos // personas ; sobran = elementos % personas
# Salida: Elementos por persona y sobrantes

elementos = int(input("Cantidad de elementos: "))
personas = int(input("Número de personas: "))
cada_uno = elementos // personas
sobran = elementos % personas
print("Cada persona recibe:", cada_uno)
print("Sobran:", sobran)