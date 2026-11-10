# Ejercicio 01: Clasificación de una nota 
# Enunciado: Clasificar una nota de 0 a 5: Bajo (<3), Básico (<4), Alto (<4.6) y Superior (resto).
# Entrada: Nota
# Proceso: if / elif / else en orden con operador loguico and 
# Salida: Clasificación

nota = float(input("Ingrese la nota de 0 a 5: "))
if nota < 3:
    print("Bajo")
elif nota >= 3 and nota < 4:
    print("Básico")
elif nota >= 4 and nota < 4.6:
    print("Alto")
else:
    print("Superior")
# tambien no es necesario usar el operador loguico and, porque se evalua las condiciones en orden
#cuando llega a la condicion elif el codigo ya sabe que la annterior condicion no se cumplio.
# nota = float(input("Ingrese la nota de 0 a 5: "))
# if nota < 3:
#     print("Bajo")
# elif nota < 4:
#     print("Básico")
# elif nota < 4.6:
#     print("Alto")
# else:
#     print("Superior")