'''generar listas'''
#primero lista del 1 al 20
#segundo lista hasta 1 millon
#tres con la lista de 1millon mirar el minimo, maximo y la suma de la lista
#cuatro numeros inpares del 1 al 20
#cinco miltiplos de 3 del 1 al 30
#seis lista con los numeros del 1 al 10 al cubo ^3
#siete lista por compresion de los cuadrados 1 al 20

primero = list(range(1, 21))
print(primero)
segundo_millon = list(range(1, (100**3)+1))
print(min(segundo_millon))
print(max(segundo_millon))
print(sum(segundo_millon))
impares = []
for imp in range(2, 22, 2):
    impares.append(imp-1)
print(impares)
mltiplos_3 = list(tre*3 for tre in range(1, 31))
print('»»')
print(mltiplos_3)
print('»»')
cubo = []
for cib in range(1, 11):
    cubo.append(cib**3)
print(cubo)
print('»»')
cuadrados = list(rad**2 for rad in range(1, 11))
print(cuadrados)
print('»»»')
text = 'python programming'
count = 0
for char in text:
    if char in 'aeiou':
        count += 1
print(count)
