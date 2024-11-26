respu="si"
while respu.lower() =="si" or respu.lower() == "SI" or  respu.lower() =="yes":
    cal1=float(input("Digitar la calificacion 1."))
    cal2=float(input("Digitar la calificacion 2."))
    cal3=float(input("Digitar la calificacion 3."))
prom=round((cal1+cal2+cal3)/3,2)

if prom >=3.0:
        estado="Aprueba++"
        
else:
        estado="Reprueba--"
        print("El promedio es ={} y el estado es ={}".format(prom,estado))
        respu=input("Desea calcular otras 3 calificaciones?: (si/no)")
        
        
        
        