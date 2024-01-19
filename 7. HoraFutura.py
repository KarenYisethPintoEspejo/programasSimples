#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
horaactual = int(input("Introduzca la hora actual: \n"))
numerohoras = int(input("Introduzca la cantidad de horas: \n"))
horafutura = (horaactual + numerohoras)%24
print (f"Dentro de {numerohoras} hora(s) sera(n) la(s) {horafutura}")
