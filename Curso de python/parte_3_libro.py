'''trabajo con listas y bucles'''
AMIGOS = ['Sunless', 'Santa', 'Sombra', 'Kai', 'Effie']

#pasar por todas las entradas de una lista, realizando la misma acción.

for amigo in AMIGOS:
    print(amigo)

'''bules'''

for amigo in AMIGOS:
    print(f'{amigo}, Tu pesadilla acaba de comenzar')
    print(f'Recuerda {amigo}; En la costa olvidada solo el acero recuerda')
print(f'¡Adiós {amigo}!')
#puede usar un bucle para realizar una acción repetitiva, como imprimir un mensaje para cada amigo en la lista.
#En este caso, el bucle for itera sobre cada elemento de la lista AMIGOS y ejecuta el bloque de código dentro del bucle para cada amigo.
print('Buena suerte')
'''range'''
#range() es una función incorporada en Python que se utiliza para generar una secuencia de números.
# La función range() puede tomar uno, dos o tres argumentos: start, stop y step.
#»»»»»
# Si solo se proporciona un argumento, se interpreta como el valor de stop y start se establece en 0.
# La función range() devuelve un objeto iterable que genera una secuencia de números en el rango especificado. Por ejemplo, range(5) generará los números del 0 al 4, mientras que range(1, 6) generará los números del 1 al 5.
for i in range(5):
    print(i)
print('»»»»')
# Si se proporcionan dos argumentos, el primer argumento se interpreta como start y el segundo como stop.
for i in range(5, 11):
    print(i)
print('»»»»')
# Si se proporcionan tres argumentos, el primer argumento se interpreta como start, el segundo como stop y el tercero como step(paso).
for i in range(0, 11, 2):#imprime los números pares del 0 al 10, ya que el paso es de 2.
    print(i)
# El argumento step se utiliza para especificar el incremento entre los números generados. Por ejemplo, range(0, 11, 2) generará los números pares del 0 al 10 (0, 2, 4, 6, 8, 10).
print('»»»»')
# La función range() es comúnmente utilizada en bucles for para iterar(recorrerlos uno por uno) sobre un rango de números o para generar índices para acceder a elementos de una lista.
# Por ejemplo, 
for i in range(len(AMIGOS)):
    print(f'Índice {i}: {AMIGOS[i]}')
#iterará sobre los índices de la lista AMIGOS, permitiendo acceder a cada amigo utilizando AMIGOS[i]

'''enumerate,
enumerate() es una función incorporada en Python que se utiliza para iterar sobre una secuencia (como una lista) y obtener tanto el índice como el valor de cada elemento en la secuencia. La función enumerate() devuelve un objeto iterable que genera tuplas, donde cada tupla contiene un índice y el valor correspondiente de la secuencia.
'''
seasons = ["Spring", "Summer", "Fall", "Winter"]

for i in range(len(seasons)):  # [consider-using-enumerate]
    print(i, seasons[i])
print('»»»»')
for i, season in enumerate(seasons): #introduce el indice y el valor en dos variables, diferente a la parte anterior que solo introducia todo en la variable i como una tupla
    print(i, season)
print('»»»»')
# En este ejemplo, el primer bucle utiliza range(len(seasons)) para iterar sobre los índices de la lista seasons, mientras que el segundo bucle utiliza enumerate(seasons) para obtener tanto el índice como el valor de cada elemento en la lista.
# El resultado de ambos bucles será el mismo, pero el uso de enumerate() es más conciso y legible.

'range() en list()'
codigo = list(range(1, 22))
print(codigo)


score = []
for i in range(5):
    score.append(int(input(f'Ingrese la puntuación {i+1}: ')))
print(f'Las puntuaciones ingresadas son: {score}')

record = []
for num in range(1, 21): #la variable extra no es necesaria pero puede tener utilidad en otro momento, "simple antes que complejo"
    records = num**2
    record.append(records)
print(f'Los cuadrados de los números del 1 al 20 son: {record}')

'''extra para la lista de numeros'''
min(record) #numero minimo de la lista
max(record) #numero maximo de la lista
sum(record) #suma de los numeros de la lista

#meter todo en una sola linea con list comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)
