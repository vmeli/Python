#declarar variables
miEdad = 0 ; tuEdad = 0 #entero
#INICIO
print( "Ingresar mi Edad:")
miEdad = int( input() ) # lectura (de frente pide dato sin necesidad de pedir número)
print( "Ingresar tu Edad:")
tuEdad = int( input() ) # lectura (---""---)
if ( miEdad > tuEdad ) : # condicional si
	print( "Soy mayor que tú") # escritura
else : #sino
	if (miEdad == tuEdad ): #si
		print( "Tenemos la misma edad")
	else: #sino
		print( "Soy menor que tú")

#FIN