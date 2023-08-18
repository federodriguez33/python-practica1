"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

area = lado_cuadrado * lado_cuadrado

print(area)

"""
Re-Escribir usando el operador de potencia.
"""

area = lado_cuadrado ** 2

print(area)

"""
Re-Escribir usando la función pow.
"""

area = pow(lado_cuadrado, 2)

print(area)

"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO

cantidad_a_comprar = presupuesto_disponible // precio

# COMPLETAR - FIN

print(cantidad_a_comprar)

"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO

es_divisible_por_siete = numero_incalculable%7

# COMPLETAR - FIN

print(es_divisible_por_siete)