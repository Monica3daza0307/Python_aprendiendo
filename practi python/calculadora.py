#REALIZAR UNA CALCULADORA DE SUMA Y RESTA
def sumar(num1,num2):
    return num1+num2

def restar(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):
    return num1/num2

while True:
    operacion=int(input("Ingrese el numero de la operacion: \n1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir"))
    if operacion not in range(1,5):
        print("Opcion equivocada")
        continue
    num1 = float(input("Digite el primer numer para realizar operacion: "))
    num2 = float(input("Digite el segundo numer para realizar operacion: "))
    
    if operacion ==1:
        resultado=sumar(num1, num2)
        print("El resultado total es: ",resultado)
    elif operacion ==2:
        resultado=restar(num1,num2)
        print("El resultado total es: ",resultado)
    elif operacion ==3:
        resultado=multiplicar(num1,num2)
        print("El resultado total es: ",resultado)
    elif operacion ==4:
        resultado=dividir(num1,num2)   
        print("El resultado total es: ",resultado)

    continuar = input("Quiere continuar utilizando la calculadora? (si/no)")
    if continuar.lower()!="s":
        break

    print("Gracias por utilizar la calculadora")