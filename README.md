# Plan de mejoramiento – Algoritmia con Python

Repositorio con los ejercicios resueltos del plan de mejoramiento de Algoritmia, organizados por temas (del 1 al 10), la actividad integradora y los diagramas de flujo en **DFD** del primer ejercicio de cada tema.
## Información del aprendiz
 **Nombre:** Danier Andres Hurtado Caicedo
 **Programa:** Análisis y Desarrollo de Software (ADSO)
 **Ficha** 3435105
 **Institución:** Servicio Nacional de Aprendizaje (SENA)

Cada ejercicio `.py` incluye en sus comentarios el **enunciado**, la **entrada**, el **proceso** y la **salida**.

## Estructura del proyecto

```
plan-mejoramiento-algoritmia-python/
├── Tema 1. Algoritmos y análisis de problemas/        (7 ejercicios)
├── Tema 2. Variables y tipos de datos/                (6 ejercicios)
├── Tema 3. Entrada y salida de información/           (4 ejercicios)
├── Tema 4. Operadores aritméticos/                    (4 ejercicios)
├── Tema 5. Operadores relacionales y lógicos/         (4 ejercicios)
├── Tema 6. Seguimiento, pruebas y corrección de errores/  (4 ejercicios)
├── Tema 7. Condicional simple,if/                     (4 ejercicios)
├── Tema 8. Condicional doble.if-else/                 (4 ejercicios)
├── Tema 9. Condicional múltiple. if-elif-else/        (4 ejercicios)
├── Tema 10. Condiciones compuestas y condicionales anidadas/  (4 ejercicios)
├── Actitividad integradora/                           (soluccion.py)
├── DFD/                                               (diagramas T1 a T10 + integradora)
└── README.md
```
*Nota: El documento en Word con las capturas de pantalla del código, ejecuciones y diagramas DFD se encuentra incluido dentro de este mismo repositorio.*

## Cómo ejecutar los ejercicios en Python

Requiere **Python 3** instalado.

```bash
python "Tema 1. Algoritmos y análisis de problemas/ejercicio_1.py"
```

Cada programa pide los datos con `input()` y muestra el resultado con `print()`.

### Cómo usarlos

1. Abrir el programa **DFD**.
2. Archivo → Abrir y elegir el `.dfd`.
3. Ejecutar e ingresar los datos que pide.

**Importante:** DFD interpreta lo que se escribe como una expresión, así que el **texto va entre comillas simples** (por ejemplo `'Juan'`, `'Concierto'`, `'aprendiz'`, `'si'`). Los números se escriben normales.

### Diferencias entre DFD y Python

- **`elif`:** DFD no lo tiene; se representa con decisiones anidadas (T9 y el descuento de la integradora). La lógica es equivalente.
- **`.lower()`:** en T10 la contraseña se compara directamente con `'si'`.
- **T6:** no pide datos; asigna `nota1 = 4.0` y `nota2 = 3.0`, igual que el código.
- **Tipos de datos:** DFD no pide `int`, `float` ni `str`; el tipo se deduce de lo que se ingresa.

---

## Resumen

| Elemento | Cantidad |
|---|---|
| Temas | 10 |
| Ejercicios en Python | 45 |
| Actividad integradora | 1 |
| Diagramas DFD | 11 |
