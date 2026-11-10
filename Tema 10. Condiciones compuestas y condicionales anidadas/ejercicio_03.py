# Ejercicio 03: Requisito de acceso
# Enunciado: Solicitar si una persona está inscrita y si presentó identificación. Mostrar si cumple ambos requisitos con and.
# Entrada: Inscrita (si/no) e identificación (si/no)
# Proceso: if inscrita and identificacion
# Salida: Cumple o no cumple

inscrita = input("¿Está inscrita? (si/no): ").lower() == "si"
identificacion = input("¿Presentó identificación? (si/no): ").lower() == "si"
if inscrita and identificacion:
    print("Cumple ambos requisitos")
else:
    print("No cumple los requisitos")
