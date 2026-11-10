# Ejercicio 07: Recaudo de una actividad
# Enunciado: Solicitar el número de participantes y el valor de inscripción por persona. Calcular el recaudo total.
# Entrada: Número de participantes y valor de inscripción
# Proceso: recaudo = participantes * valor
# Salida: Recaudo total

participantes = int(input("Número de participantes: "))
valor = float(input("Valor de inscripción por persona: "))
recaudo = participantes * valor
print("El recaudo total es:", recaudo)