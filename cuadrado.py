# ------------------
# n = input('Ingrese el número')
# n = float(n)
# a = n**2
# r = a%2
# print(r)
# -----------------

#nombre de algoritmo : es el nombre del archivo

#declaracion de variables (simular debemos poner un valor a la variable)
#n = 0 #print( type( n ))

#declaracion de variables 
n = 0; cuadrado = 0; resto = 0  #entero

#INICIO
print( "Ingrese número:") 
n = input() #lo lee como cadena
n = int( n ) #lo convertimos a entero 
cuadrado = n * n #elevamos al cuadrado
resto = cuadrado % 2 #obtenemos resto respecto a 2
print( "resultado: ", resto ) #mostramos resultado
#FIN



