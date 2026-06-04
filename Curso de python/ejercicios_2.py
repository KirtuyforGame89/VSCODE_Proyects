# Ejercicio 2: Lista de amigos
LISTA_AMIGOS = ['Sunless', 'Casse', 'Nephis', 'Kai', 'Effie']
print(f'Amigos invitados a mi cumpleaños: {LISTA_AMIGOS}')
print(f'Número de amigos invitados: {len(LISTA_AMIGOS)}')
print(f'Invitado especial: {LISTA_AMIGOS[0]}')
#Cambio en la lista de amigos
print('¡Oh no! Nephis no podrá venir a la fiesta.')
LISTA_AMIGOS[2] = input('Nephis no vendra porque sigue atrapada en "La Costa Olvidada"\n¿Quién quieres que la reemplace? ')
print(f'Lista actualizada de amigos nueva: {LISTA_AMIGOS}')
#Nuevo amigo agregado
print('Acabamos de agrandar el lugar de la fiesta, asi que vamos a invitar 1 amigo mas')
LISTA_AMIGOS.append(input('Ingresa el nombre de un nuevo amigo: '))
print(f'Lista actualizada: {LISTA_AMIGOS}')
#Más amigos invitados
print('¡Buenas noticias! Hemos conseguido un lugar aún más grande, así que podemos invitar a 2 amigos más.')
LISTA_AMIGOS.insert(0, input('Ingresa el nombre de un nuevo amigo para el inicio de la lista: '))
LISTA_AMIGOS.insert(len(LISTA_AMIGOS), input('Ingresa el nombre de un nuevo amigo para el final de la lista: '))
print(f'Lista actualizada: {LISTA_AMIGOS}')
#Reducción de invitados
print('·······')
print('¡Oh no! El lugar de la fiesta se ha reducido y solo podemos invitar a 2 amigos.')
while len(LISTA_AMIGOS) > 2:
    amigo_eliminado = LISTA_AMIGOS.pop()
    print(f'Lo siento {amigo_eliminado}, no podrás asistir a la fiesta.')
print(f'Amigos que aún pueden asistir: {LISTA_AMIGOS}')
LISTA_AMIGOS.clear()
print(f'Lista final de amigos: {LISTA_AMIGOS}')
#the game