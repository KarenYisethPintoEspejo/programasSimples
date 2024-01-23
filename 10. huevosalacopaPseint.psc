Algoritmo huevosalacopa
	Definir TH Como Real
	T <- 20
	TE <- 100
	M <- 47
	densidad <- 1.038
	C <- 3.7
	k <- 0.0054
	Escribir "Ingrese la temperatura del huevo"
	Leer TH
	Definir dividendo, divisor, resultado,resultado2,segundoos, minutos Como Real
	dividendo <- (M^(2/3))*(C*densidad^(1/3))
	divisor <-(k*(pi^2))*((4*pi)/(3))^(2/3)
	resultado <- dividendo/divisor
	resultado2 <- ln(0.76*(TH-TE)/(70-TE))
	segundoss <- resultado*resultado2
	minutos <- redon(segundoss/60)
	Escribir "El tiempo para prepararlo a la copa es de " segundoss, " segundos"
	Escribir "El tiempo para prepararlo a la copa es de " minutos " minutos"
	
FinAlgoritmo
