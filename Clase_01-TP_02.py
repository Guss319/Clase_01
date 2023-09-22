from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def elevar_al_cuadrado(x):
    return x ** 2

def es_par(x):
    return x % 2 == 0

def suma(x, y):
    return x + y

# Usar map para elevar al cuadrado todos los números
cuadrados = list(map(elevar_al_cuadrado, numeros))

# Usar filter para obtener solo los números pares
numeros_pares = list(filter(es_par, numeros))

# Usar reduce para sumar todos los elementos de la lista
suma_total = reduce(suma, numeros)

# Resultados
print("Lista original:", numeros)
print("Cuadrados de los números:", cuadrados)
print("Números pares:", numeros_pares)
print("Suma total de la lista:", suma_total)


### se utiliza la funcion map para generar una lista que muestre todos los numeros de la lista "numeros" al cuadrado
### se utiliza la funcion filter para seleccionar todos los numeros pares de la lista "numeros"
### se utilizs ls funcion reduce para sumar todos los numeros de la lista "numeros"