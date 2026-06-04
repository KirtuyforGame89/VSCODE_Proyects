#variables . son contenedores o etiquetas para la informacion que se les asigne 

gato = 'moshi'
gato_webon = 'Gueon'
sork = 22
metro = 100
mark = 'panecio'

#variable y imprimir texto en pantalla
print('the game nigger')
merk = 'tonto webon kuliao'
print(merk)
merk = 'lo siento weon kulia'
print(merk)
print('###################')
#cadenas de texto: cualquier cosa que este entre "" es una cadena
name = 'kirtuy nuremberg'
tork = 'Warhammer 40k es un universo de ciencia ficcion y fantasia oscura para adultos o GrimDark como suele se referido....'
print(name.title()) #cambia cada palabra a formato de titulo, cada palabra con la primera mayuscula
print(name.upper()) #todo mayuscula
print(name.lower()) #todo minuscula 

#cadena f' 
name = 'kirtuy nuremberg'
locasion = 'Santander'
eda = 23
individuo = f'El sujeto {name} de edad {eda} ubicado en {locasion}: '

print(individuo.title())

#tabulacion: cualquier espacion que no se imprima (espacio, tab, fin de linea)
#añadir una tablacion '\t'
print('Instrucciones')
print('\tInstrucciones')
#nueva linea en una cadena '\n' 
print('\tInstrucciones: \nSaltar \nAgacharse \nRecoger \nMoverse \n>>>>')
#nueva linea + tabulacion '\n\t'
print('\tInstrucciones: \n\tSaltar \n\tAgacharse \n\tRecoger \n\tMoverse \n\t>>>>')
print('_______')
#eliminar espacios a la derecha ".rstrip()" o izquierda ".lstrip()" de la cadena en una variable 
locasion_fisica = ''' casa ''' #espacio al principio y al final
de_quien = 'mi agradable'
color = 'blanco'
print(de_quien + locasion_fisica + color)
print(de_quien + locasion_fisica.rstrip() + color + '<<<elimina el espacio a la derecha de la variable>>>') #elimina el espacio a la derecha de la variable
print(de_quien + locasion_fisica.lstrip() + color + '<<<elimina espacio a la izquierda>>>')#elimina espacio a la izquierda
print(de_quien + locasion_fisica.strip() + color + '<<<elimina ambos espacios>>>')   #elimina ambos espacios
print('___novo__\n\t_')


'''                     _______
                       /       \\
                      .==.    .==.
                     ((  ))==((  ))
                    / "=="    "=="\\
                   /____|| || ||___\\
       ________     ____    ________  ___    ___
       |  ___  \\   /    \\   |  ___  \\ |  |  /  /
       |  |  \\  \\ /  /\\  \\  |  |  \\  \\|  |_/  /
       |  |   )  /  /__\\  \\ |  |__/  /|  ___  \\
       |  |__/  /  ______  \\|  ____  \\|  |  \\  \\
_______|_______/__/ ____ \\__\\__|___\\__\\__|___\\__\\____
|  ___  \\ |  ____/ /    \\   |  ___  \\ |  ____|  ___  \\
|  |  \\  \\|  |___ /  /\\  \\  |  |  \\  \\|  |___|  |  \\  \\
|  |__/  /|  ____/  /__\\  \\ |  |   )  |  ____|  |__/  /
|  ____  \\|  |__/  ______  \\|  |__/  /|  |___|  ____  \\
|__|   \\__\\____/__/      \\__\\_______/ |______|__|   \\__\\

'''
#eliminar prefijos 
annas_archive_url = 'https://annas-archive.gd/'
print(annas_archive_url)
annas_archive_url = annas_archive_url.removeprefix('https://')  #elimina desdeel principio de la variable
print('Anna')
print(annas_archive_url.removesuffix('/'))  #elimina desde el final
print(annas_archive_url)

#error sintáctico '', "", ???,
#solamente tener en cuenta estos errores y no escribir como un mono anti gramatica

#numeros: en general solo operaciones normales 
suma = 2+2
resta = 7-2
multiplicacion = 2*2
division = 10/12
exponente = 2**3
division_entera = 3//2      #esta division devuelve el numero entero aproximado

#floats: cualquier numero con desimales se considera float 
#el resultado de cualquier operacion que contenga un numero float sera float
seth_1 = 2+3*4
seth_2 = 2.5*4
seth_3 = 0.1+0.1
seth_4 = 0.7+3.4 

#algunos resultados pueden dar resultados con 
seth_5 = 0.2+0.1
seth_6 = 3*0.1

#guiones en numeros
#se pueden agrupar los numeros con guines ,independiente de la posicion del guion en el nuemero 
# python o sigue leyendo con normalidad ya que ignora los guiones

merk = 1_000_000_000
mork = 23_00_0000_00

#asignacion multiples
#se pueden asignar valores a mas de una variable en una misma linea
sirk, serk, firk, ferk = 1, 2, 3, 4
#tambien funciona con variables que tengan valores 
sork = sirk, serk, firk, ferk, 7, 8, 9
print("____")
print(sork)
LO, LI, LP, LM, LJ, LF, LT = sork
#python no tiene constantes integradas 
#la buena costumbre es poner la variable en MAYUSCULA para que se entienda que no se debe cambiar
MERT = "webos"
if sirk >= seth_6:
    print('webos')



