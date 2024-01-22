#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final.

c1 = float(input("Introduzca la nota del primer certamen: \n"))
c2 = float(input("Introduzca la nota del segundo certamen: \n"))
nl = float(input("Introduzca la nota de laboratorio: \n"))

nc = (10*60-3*nl)/7
c3= 3*nc-c1-c2

print(f"Necesita una nota de {c3} en tu tercer certamen")