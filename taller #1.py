


# punto 1
multiploTres = []
multiploDos = []
cantidadNumeros = int(input('Dijite la cantidad de numeros que desea evaluar: '))
for i in range(cantidadNumeros):    
    numeroIngresado = int(input('Digite un numero:' ))
    if(numeroIngresado%3 == 0):
        multiploTres.append(numeroIngresado)
    if(numeroIngresado%2 == 0):
        multiploDos.append(numeroIngresado)

print(f'los multiplos de dos son: {multiploDos}')
print(f'los multiplos de tres son: 3{multiploTres}')


# punto dos

