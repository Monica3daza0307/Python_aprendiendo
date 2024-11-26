    #Un empleado tiene derecho al almuerzo como incentivo por llegar puntual al trabajo (llegar puntual es llegar antes de 8:00 AM), realizar un algoritmo que muestre los días que tienen y que no tiene derecho con la empresa (recomenzación, usar cico for y continue)

dias_laborales=int(input("Ingrese numero de días laborados: "))
dias_con_almuerzo=0
dias_sin_almuerzo=0

for dia in range(1,dias_laborales +1):
    hora=int(input(f"Ingrese la hora de llegada del día {dia}"))
    if hora < 8:
        dias_con_almuerzo+=1
    else:
        dias_sin_almuerzo+=1
print(f"Días con derecho a almuerzo: {dias_con_almuerzo}")
print(f"Días sin derecho a almuerzo: {dias_sin_almuerzo}")
    