# Ejercicio 06: Costo de impresión
# Enunciado: Solicitar el número de páginas y el precio por página; calcular el costo de la impresión.
# Entrada: Número de páginas y precio por página
# Proceso: costo = paginas * precio_pagina
# Salida: Costo de la impresión

paginas = int(input("Número de páginas: "))
precio_pagina = float(input("Precio por página: "))
costo = paginas * precio_pagina
print("El costo de la impresión es:", costo)