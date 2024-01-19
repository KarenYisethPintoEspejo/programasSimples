#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
numeronormal = input("Introduzca un numero entero de 3 digitos: \n")
numeroinvertido = int(str(numeronormal[::-1]))
print(f"El numero invertido es: {numeroinvertido}")