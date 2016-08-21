#declaramos variables
nota = 0.0 # se declara asi por ser un real verificamos con print( type( nota ))
#inicio
nota = float( input() ) #lectura

if( nota >=17 and nota <=20 ) : #[17, 20]
	print("AD")
else : #< -inf , 16 ] or [ 21 ,...inf>
	if( nota >= 14 and nota <=16 ) : #[14,16]
		print( "A")
	else : #< -inf , 13 ] or [ 21, inf>
		if( nota >= 11 and nota <=13 ) : #[ 11, 13 ]
			print( "B")
		else : #< -inf , 10 ] or [ 21, inf>
			if ( nota >=0 and nota <= 10) : #[0, 10]
				print( "C")
			else : #< -inf , -1 ] or [ 21, +inf>
				print( "nota inválida")
#fin