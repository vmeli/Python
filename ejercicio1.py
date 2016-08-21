#código prof
#declaramos variables
nota = 0
#INICIO
nota = int( input() ) #float para que sea real
if ( nota >= 17): #[ 17 , 20 ]
	print("AD")
else: #[ 0 , 16 ]
	if ( nota >= 14 ) : #[ 14 , 16 ]
		print("A")
	else: #[ 0 , 13 ]
		if ( nota >= 11 ): #[ 11, 13 ]
			print("B")
		else : #[ 0 , 10 ]
			print("C")
#FIN


print("Ingrese la nota del alumno:")
a = int(input())

# Llegue a codificar
# nota = int(input("Ingrese la nota del alumno: "))
# if (nota>=0 and nota<=20):
# 	if(nota>=11 and nota<=13):
# 		print("Equivale B")
# 	else:
# 		if(nota>=14 and nota<=16):
# 			print("Equivale A")
# 		else:
# 			if (nota>=17 and nota<=20):
# 				print("Equivale AD")
# 			else:
# 				print("Equivale C")
# else:
# 	print("La nota no esta en el rango de 0 y 20")