# Ejercicio 04: Beca de estudio
# Enunciado: Solicitar el promedio y si tiene matrícula activa. Cumple los requisitos preliminares si promedio >= 4.5 y matrícula activa.
# Entrada: Promedio y matrícula activa (si/no)
# Proceso: if promedio >= 4.5 and activa
# Salida: Cumple o no los requisitos preliminares

promedio = float(input("ingrese su promedio Promedio: "))
activa = input("¿Tiene matrícula activa? (si/no): ").lower() == "si"
if promedio >= 4.5 and activa:
    print("Cumple los requisitos preliminares para la beca")
else:
    print("No cumple los requisitos preliminares")
