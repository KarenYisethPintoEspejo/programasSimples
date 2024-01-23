Algoritmo numeroinvertido
	Definir n,x,c Como Entero
	Definir a,suma Como Real
	Escribir "Ingresa un numero entero de 3 digitos"
	leer n
	a = 100
	suma = 0
	c = 0
	Mientras n>0 Hacer
		x = n mod 10
		n = trunc(n/10)
		suma = suma+x*a
		a = a/10
		c=c+1
	FinMientras
	si c==3 Entonces
		Escribir "El numero es de tres cifras ", suma
	SiNo
		Escribir "El numero no es de tres cifras " 
		
	FinSi
	
FinAlgoritmo
