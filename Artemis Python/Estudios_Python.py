#0.2 Archivo para hacer apuntes sobre lo que voy aprendiendo de python
print("The game ") #mostrar texto 

#Tipos de datos y estructuras basicas
"""
texto entre lineas "me parece diferenteel uso de comentario y hacer este texto entre lineas"
"""
#bool (bolianos)
verdadero = True
falso = False

# f-string: la forma moderna de formatear texto
nim, eda = "Kirtuy" , 34
print('nombre {}, edad: {}' .format(nim, eda))
print('nombre %s, edad: %d' %(nim, eda))
print(f"resultado. {nim}, {eda} anos")

#numeros
enteros = -2,-1,0,1,2 #int 
desimales = 1/3,3.4,1.5 #float 
complejos = 1 + 3j #complex number

print(type(eda))
print('num')
print(enteros)

# funciones 

maldis = "crim o corrupsa?"

#  '.is' devuelve bool comprivando la condicion que se aplique, ejemplo ai ea mayuacula o minusula

print(maldis.capitalize())  #primera letra en mayuscula
print(maldis.count('r'))    #cantidad de () tiene
print(maldis.isnumeric())   #pregunta si es un numero - devuelve false
print('1'.isnumeric())      #devuelve true
print(maldis.lower())       #todo minuscula
print(maldis.upper())       #todo mayuscula
print(maldis.upper().isupper()) #devuelve bool si es mayuscula

