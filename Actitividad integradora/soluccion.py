# Actividad Integradora: Cálculo de Compra en Papelería con Descuentos por Rangos
# 1. Enunciado del problema:
# Una papelería local requiere un programa para calcular el total a pagar por la compra de cuadernos. 
# Si se compran menos de 5 cuadernos no hay descuento; si se compran de 5 a 9 se aplica un 
# 10% de descuento; y si se compran 10 o más se aplica un 15% de descuento sobre el subtotal. 
# Adicionalmente, se suma un envío de $5,000 si el subtotal es menor a $50,000; de lo contrario es gratis.
# 2. Identificación de entradas, procesos y salidas:
# - Entradas: Cantidad de cuadernos (int) y precio unitario (float).
# - Procesos: Calcular subtotal, evaluar rangos con if-elif-else para el descuento y condicional para el envío basado en el subtotal.
# - Salidas: Subtotal, descuento aplicado, costo de envío y total final a pagar.

cantidad_cuadernos = int(input("ingrese la cantidad de cuadernos:"))
precio_unitario = float(input("ingrese el precio unitario de los cuadernos:"))
sub_total = cantidad_cuadernos * precio_unitario
if  cantidad_cuadernos < 5:
    descuento = 0
elif cantidad_cuadernos <= 9:
    descuento = sub_total * 0.10
else:
    descuento = sub_total * 0.15
total_parcial = sub_total - descuento
if sub_total < 50000:
    envio = 5000
else:
    envio = 0 
total_final = total_parcial + envio
print("---FACTURA DE COMPRA---")
print("sudtotal es:",sub_total)
print("su descuento es de:",descuento)
print("el costo del envio es:",envio)
print("el total a pagar es:",total_final)    

    