#Experimentar con las listas

### listas ### - 'Arreglos'

merk = [ 0, 1, 2, 3, 4, 5, 56, 2, 2, 65, 7]
yark = ['futa', 22, 'sunless', 18]
sork = list()

print(len(merk))

print(yark)
print(merk)
print(sork)

print(yark[0])
print(yark[3], 'cm')

print(len(yark))
yark.insert(22,'shadow')        #agrega un elemento en la posion indicada primero o nombrando el elemento de la lista al que quiere suceder el nuevo elemento
print(yark)
print(len(yark))

hent, dud, sunny, ded, sun = yark
print(hent)
print(dud)
print(sunny)
print(ded)
print(sun)
print(yark)

#sigo experimentando

print(yark + sork + merk)

yark.append('burn')     #agrega un elemento al final
print(yark)

print('sé eliminó: ',yark.pop())        #saca un elemento de la ultima posicion y lo retorna(lo muestra)
print(yark)

del yark[4]     # 'del' elimina elementos segun el indice
print(yark)

print(merk)
merk.remove(2) # elimina el elemento espesifico, en orden de izquierda a derecha (si el elemento se repite en la lista solo elimina 1)
print(merk)
print('webos')


phoss = yark.copy() #caso raro con el copy ,la nueva variable se queda con el contenido pero aunque se limpie la anterior variable esta nueva no cambia

yark.clear()
print(yark)
print(phoss)

phoss.reverse() #da vuelta a la lista
print(phoss)

print(merk[2:6])    #saca  una parte de la lista en espesifico
print(merk)

merk.sort()     #ordena  la lista (en orden de menor a mayor segun biene predeterminado)
print(merk)

###tulpass (tupla)xd ###
print('Tuplas')

tupmark = tuple()
tupomark = ()
tupomark = (0, 1, 2, 3, 4, 5, 56, 2, 2, 65, 7)
#de momento no es diferente a una lista 
tupark = ('lim', 222, 'tip', 8, 3, 3, 3, 'siu', '3m', 3, 15)
print(tupark)
print(type(tupark))

print(tupark[0])

print(tupark.count(3))#cuantos elementos hay en esta tupla
print(tupark.index('siu'))  #dice em que posicion esta este elemento 
print(tupark)
#las tuple por definicion no son mutables , que no se puden modificar a diferencia de las listas
#se pueden convinar tuplas em una nueva tuple pero no se puede modificar 
tetopark = tupark + tupomark

print(tetopark)
print(type(tetopark))
print(tetopark[0:4])

#transformar tuple en liata
tetopark = list(tetopark)
print(tetopark)
print(type(tetopark))

del tetopark[0]
del tetopark[1]
del tetopark[5]
del tetopark[5]


tetopark.sort()
print(tetopark)
tetopark = tuple(tetopark)
print(type(tetopark))
print(tetopark)

