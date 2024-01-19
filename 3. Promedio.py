#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
nota1 = float(input(f"Introduzca la primera nota: \n"))
nota2 = float(input(f"Introduzca la segunda nota: \n"))
nota3 = float(input(f"Introduzca la tercera nota: \n"))
nota4 = float(input(f"Introduzca la cuarta nota: \n"))

promedio = ((nota1+nota2+nota3+nota4)/4)

print(f"El promedio de sus notas es: {promedio}")