# Ejercicio 04: Requisitos de inscripción
# Enunciado: Solicitar la edad y si tiene documento vigente. Construir una expresión con and: mayor de edad y documento vigente.
# Entrada: Edad (int) y si tiene documento vigente (str)
# Proceso: Evaluar si es mayor de edad (>= 18), verificar si el documento es "si" y combinar ambas condiciones con and
# Salida: True o False indicando si cumple los requisitos de inscripción


edad = int(input("Ingrese la edad: "))
documento = input("¿Tiene documento vigente? (si/no): ")
es_mayor_edad = edad >= 18
tiene_documento = documento == "si"
cumple = es_mayor_edad and tiene_documento
print("¿Cumple los requisitos de inscripción?", cumple)