#declaro variables
n = 0; nota = 0; sumaNotas = 0; maximo = 0; minimo = 20 # el valor de minimo puede ser negativo y el valor de maximo puede exceder a 20
#inicio
print( "Cantidad de notas: " )
n = int( input() )
for i in range ( 1 , n+1 , 1 ):
    print( "Ingrese la nota nro ", i )
    nota = int( input() )
    maximo = max( maximo , nota ) #obtenemos el máximo
    minimo = min( minimo , nota ) #obtenemos el mínimo
    sumaNotas = sumaNotas + nota

#print( max( 4, 10) )

print( "El promedio de notas es: ", sumaNotas/n )
print( "La máxima nota es: ", maximo )
print( "La mínima nota es: ", minimo )


# print("Ingrese las cantidad de notas")
# n = int(input())
# suma = 0
#
# for i in range ( 1 , n+1, 1):
#     print("ingrese la nota ", i)
#     nota = int(input())
#     suma = suma + nota
#
# promedio = suma/n
#
# print(promedio)
