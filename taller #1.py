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
print('Ingrese 10 ingredeintes para preparar un salpicon.')
ingredientes =[]
for i in range(10):  
    ingredientes.append(input('Ingrese el nombre del ingrediente: '))
print('La lista de ingredientes ingresados es: ')

for i in reversed(ingredientes):
    print(i)

#punto 3
option = 10
productos = []

while(option != 0):
    producto ={
        'Codigo' : '', 
        'Nombre' : '',
        'Precio' : ''
    }
    print('La Tienda')
    print('***************')
    print('Digita 0. para salir.')
    print('digita 1. para ingresar un producto')
    print('digita 2. para mostrar los productos registrados ') 
    print('digita 3. para buscar por codigo y editar el precio ') 
    print('digita 4. para buscar por codigo y eliminar un producto ') 
    option = int(input('Digite una opcion: '))
    if(option== 1):
        producto['Nombre'] = input('Ingrese el nombre del producto: ')
        producto['Codigo'] = input('Ingrese el codigo del producto: ')
        producto['Precio'] = input('Ingrese el precio del producto: ')
        productos.append(producto)
    if(option == 2):
        print('los productos registrados son:')
        for item in productos:
            print(item)
    if(option ==3):
        codido = input('Codigo: ')
        for product in productos:
            if(product['Codigo'] == codido):
                print(product)
                product['Precio'] = input('Digite el nuevo precio: ')
            else:
                print('El producto no se encuentra registrado')

    if(option == 4 ):
        codido = input('Codigo de producto a eliminar: ')
        for product in productos:
            if(product['Codigo'] == codido):
                print(product)
                productos.remove(product)
            else:
                print('El producto no se encuentra registrado')



