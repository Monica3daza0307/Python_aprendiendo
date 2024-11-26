def valorEstatura(est):
    
    if est < 1.50:
        print("Eres una persona de estatura baja")
    else:
        print("Eres una persona alta")
        
respu="si"
while respu=="si" or respu=="SI":
    estatura=float(input("cuanto mide? "))
    valorEstatura(estatura)
    respu=input("desea continuar")
    
    

