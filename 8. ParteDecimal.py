#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
numerodecimal = float(input("Introduzca el numero real: \n"))
decimal = (numerodecimal - int(numerodecimal))
print (f"La parte decimal del numero ingresado es: {decimal}")