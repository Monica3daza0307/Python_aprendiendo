valores = [5,4,3,2,1]
encontrado = False
indice = 0
Longitud = len(valores)

while not encontrado and indice < Longitud:
    valor = valores[indice]
    if valor == 7:
        encontrado = True
    else:
        indice +=1
        
if encontrado:
    print(f'El numero 7 ha sido encontrado en  indice {indice}.')
else:
    print('El numero 7 no se ha encontrado')