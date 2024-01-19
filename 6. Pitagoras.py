#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2
catetoa = float(input("Introduzca la longitud del primer cateto: \n"))
catetob = float(input("Introduzca la longitud del segundo cateto: \n"))
hipotenusa = ((catetoa*catetoa)+(catetob*catetob))
c = (hipotenusa**0.5)

print(f"El largo de la hipotenusa es igual a: {c}")