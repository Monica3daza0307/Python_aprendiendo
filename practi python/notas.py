#Ingrese 3 notas del 1 al 10 y sacar el promedio
nota1=float(input("Digite su primer nota: "))
nota2=float(input("Digite la segunda nota: "))
nota3=float(input("Digite la tercer nota: "))

promedio=(nota1+nota2+nota3)/3

if promedio > 8:
    print("Felicitaciones")
elif 6 <= promedio <=7.9:
    print("Buen trabajo")
elif 4 <= promedio >=5.9:
    print("Deficiente")
else:
    print("Deficiente")