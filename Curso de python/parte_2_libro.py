#números ææææææ ¢¢„»»»«««»«»«»«»«xzxzxxz+alt_gr
#enteros
se = 2+3*4
re = 2.5*4
rt = 0.1+0.1
fd = 0.7+3.4
fg = 0.2+0.1
gy, mark = 3*0.1, "pasword"
#utilizar esto para listas 

MORK = 3
MERK = 'kirtuy'
print(f'!!Hola {MERK}, se te a asignado n°{MORK}')
print('Facilito no?')

# tipos de listas

LISTAS_LETRAS = ['a', 'b', 'c', 'd', 'e']
LISTAS_NUMEROS = [1, 2, 3, 4, 5]
LISTAS_MEZCLADAS = ['a', 1, 'b', 2, 'c', 3]
LISTAS_ANIDADAS = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
LISTAS_VACIAS = []
LISTAS_REPETIDAS = [1, 2, 3] * 3
LISTAS_RANGOS = list(range(1, 11))  
LISTAS_COMPRENSION = [x**2 for x in range(1, 12)]
LISTAS_COPIADAS = LISTAS_LETRAS.copy()
LISTAS_CADENA = list('Hola Mundo')
LISTAS_TUPLA = list((1, 2, 3, 4, 5))
LISTAS_DICCIONARIO = list({'a': 1, 'b': 2, 'c': 3}.items())
LISTAS_SET = list({1, 2, 3, 4, 5})
LISTAS_GENERADOR = list(x**2 for x in range(1, 11))
LISTAS_MULTIDIMENSIONALES = [[1, 2], [3, 4], [5, 6]]
LISTAS_MATRIZ = [[1, 2, 3], [4, 5, 6]]

print(LISTAS_COMPRENSION)
LISTA_AMIGOS = ['Sunless', 'Casse', 'Nephis', 'Kai', 'Effie']
print(LISTA_AMIGOS[0])  # Acceder al primer elemento
print(LISTA_AMIGOS[2])  # Acceder al tercer elemento
print(LISTA_AMIGOS[-1])  # Acceder al último elemento
print(f'Hola {LISTA_AMIGOS[1]}, ¿cómo estás?')  # Usar un elemento en una cadena
lista_vehiculos = ['coche', 'moto', 'bicicleta']
print(lista_vehiculos[0])  # Acceder al primer elemento
LISTA_AMIGOS[2] = 'Luna'  # Modificar el tercer elemento
print(LISTA_AMIGOS)  # Imprimir la lista modificada

LISTA_AMIGOS.append('Nova')  # Agregar un nuevo elemento al final de la lista
print(LISTA_AMIGOS)  # Imprimir la lista con el nuevo elemento

LISTA_AMIGOS.insert(1, 'Sol')  # Insertar un nuevo elemento
print(LISTA_AMIGOS)  # Imprimir la lista con el nuevo elemento insertado

LISTA_AMIGOS.remove('Kai')  # Eliminar un elemento por valor
print(LISTA_AMIGOS)  # Imprimir la lista después de eliminar el elemento

del LISTA_AMIGOS[0]  # Eliminar un elemento por índice
print(LISTA_AMIGOS)  # Imprimir la lista después de eliminar el elemento

LISTA_AMIGOS.pop()  # Eliminar el último elemento
print(LISTA_AMIGOS)  # Imprimir la lista después de eliminar el último elemento

LISTA_AMIGOS.pop(1)  # Eliminar el elemento en el índice
print(LISTA_AMIGOS)  # Imprimir la lista después de eliminar el elemento

LISTA_AMIGOS.clear()  # Vaciar la lista#
print(f'Limpiamos la lista: {LISTA_AMIGOS}')  # Imprimir la lista vacía#

LISTA_AMIGOS = ['Sunless', 'Casse', 'Nephis', 'Kai', 'Effie']
LISTA_AMIGOS.extend(['Luna', 'Sol'])  # Agregar múltiples elementos
print(f'Lista con nuevos elementos: {LISTA_AMIGOS}')  # Imprimir la lista con los nuevos elementos agregados
LISTA_AMIGOS += ['Nova', 'Estrella']  # Agregar múltiples elementos usando el operador +=
print(f'Lista con nuevos elementos usando +=: {LISTA_AMIGOS}')  #Imprimir la lista con los nuevos elementos agregados usando +=
print(f'Número de amigos en la lista: {len(LISTA_AMIGOS)}')  # Imprimir el número de elementos en la lista
print(f'¿Está "Luna" en la lista de amigos? {"Luna" in LISTA_AMIGOS}')  # Verificar si un elemento está en la lista
print(f'¿Está "Marte" en la lista de amigos? {"Marte" in LISTA_AMIGOS}')  # Verificar si un elemento no está en la lista

#ordenar listas
LISTA_AMIGOS.sort()  # Ordenar la lista alfabéticamente
print(f'Lista de amigos ordenada: {LISTA_AMIGOS}')  # Imprimir la lista ordenada
# Ordenar la lista en orden inverso
print(f'Lista de amigos ordenada en orden inverso: {sorted(LISTA_AMIGOS, reverse=True)}')  # Imprimir la lista ordenada en orden inverso
# Ordenar la lista por la longitud de los nombres
print(f'Lista de amigos ordenada por longitud: {sorted(LISTA_AMIGOS, key=len)}')  # Imprimir la lista ordenada por longitud
# Ordenar la lista por la última letra de los nombres
print(f'Lista de amigos ordenada por la última letra: {sorted(LISTA_AMIGOS, key=lambda x: x[-1])}') # Imprimir la lista ordenada por la última letra
print(f'Número de amigos en la lista: {len(LISTA_AMIGOS)}')  # Imprimir el número de elementos en la lista

#bucle for
print('Todos mis amigos: ')
for amigo in LISTA_AMIGOS:
    print(amigo)
for i in range(len(LISTA_AMIGOS)):
    print(f'Índice {i}: {LISTA_AMIGOS[i]}')
print('Son todos mis Amigos')
