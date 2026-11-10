# Ejercicio 5. Aplicación — Pago de un servicio
# Solicite una tarifa fija, un costo por unidad y la cantidad de unidades utilizadas. Calcule el valor total.
# Entrada: tarifa fija, costo por unidad y cantidad de unidades utilizadas 
# proceso: total = tarifa_fija + (costo_unidad * cantidad_unidades)
# salida: valor total a pagar 


tarifa_fija = float(input("ingrese la tarifa fija:"))
costo_unidad = float(input("ingrese el costo por unidades:"))
cantidad_unidades = int(input("ingrese la cantidad de unidades utilizadas:"))
total = tarifa_fija + (costo_unidad * cantidad_unidades)
print("el valor a pagar es:",total)




