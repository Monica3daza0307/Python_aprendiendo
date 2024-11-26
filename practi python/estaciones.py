estaciones=["otoño","Primavera","verano","Invierno"]
print(estaciones)

estaciones[0]="lluvioso"
estaciones.insert(3,"frio")
estaciones.append("Templado")
estaciones.pop(3)
estaciones.pop()
print(estaciones[2].upper())
print(estaciones[2].lower())
print(estaciones[1].title())
print(estaciones[2].capitalize())