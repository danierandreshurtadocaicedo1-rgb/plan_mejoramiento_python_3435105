# Ejercicio 04: Costo de envío
# Enunciado: Solicitar el valor de una compra. Si alcanza 100000 el envío es gratis; si no, cuesta 8000. Mostrar el costo del envío.
# Entrada: Valor de la compra
# Proceso: if compra >= 100000: envio = 0 / else: envio = 8000
# Salida: Costo del envío

compra = float(input("Valor de la compra: "))
if compra >= 100000:
    envio = 0
else:
    envio = 8000
print("Costo del envío:", envio)
