# Ejercicio 01: Aprobar o no aprobar 
# Enunciado: Solicitar una nota de 0 a 5. Si es >= 3 mostrar Aprobado; en caso contrario, No aprobado.
# Entrada: Nota
# Proceso: if nota >= 3 / else
# Salida: Aprobado o No aprobado

nota = float(input("Ingrese la nota: "))
if nota >= 3:
    print("Aprobado")
else:
    print("No aprobado")
