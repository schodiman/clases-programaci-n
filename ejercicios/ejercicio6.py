# 1.- Escriba un programa que pida 3 números y los ordene de mayor a menor.
def ordenar_numeros():
    try:
        numeros = []
        for x in range(3):
            numero = float(input('Ingrese número:'))
            numeros.append(numero)
        numeros.sort(reverse=True)
        print(numeros)
    except:
        print('Valor ingresado NO corresponde a un  número...')

# 2.- Escriba un programa que calcule el área y el perímetro de un cuadrado, 
# si cualquier valor es negativo, se debe entregar un mensaje de error.
def area_cuadrado():
    try:
        lado = float(input('Ingrese valor del lado: '))
        if lado >= 0:
            print(f'El área del cuadrado de lado {lado} = {round(lado * lado, 2)}')
            print(f'El perímetro del cuadrado de lado {lado} = {round(lado * 4, 2)}')
        else:
            print('No se permite ingresar valores negativos')
    except:
        print('Valor ingresado NO corresponde a un  número...')

# 3.- Escriba un programa que pida el precio de un producto y calcule el valor del IVA, 
# si el precio es negativo, se debe entregar un mensaje de error.
def calcular_iva():
    try:
        iva = 19/100
        precio = float(input('Ingrese precio del producto: '))
        if precio >= 0:
            valor_iva = precio * iva
            valor_total = precio + valor_iva
            print(f'Precio: ${round(precio)}, IVA: ${round(valor_iva)}, TOTAL: ${round(valor_total)}')
        else:
            print('No se permite ingresar valores negativos')
    except:
        print('Valor ingresado NO corresponde a un  número...')

# 4.- Escriba un programa que permita calcular el área de un triángulo, 
# si cualquier valor es negativo, se debe entregar un mensaje de error.

# 5.- Escriba una calculadora básica que pida al usuario 2 números
# y realice las 4 operaciones aritméticas básicas.
# Si se trata de dividir por 0 se deberá entregar un mensaje de error.
def calculadora_basica():
    try:
        operaciones = ['+','-','*','/']
        numero_1 = float(input('Ingrese primer númereo: '))
        numero_2 = float(input('Ingrese segundo número: '))
        for op in operaciones:
            if op == '/' and numero_2 != 0:
                resultado = eval(str(numero_1) + op + str(numero_2))
                print(f'{numero_1} {op} {numero_2} = {round(resultado,2)}')
            elif op == '+' or op == '-' or op == '*':
                resultado = eval(str(numero_1) + op + str(numero_2))
                print(f'{numero_1} {op} {numero_2} = {round(resultado,2)}')        
            else:
                print('No se puede dividir por 0')
    except:
        print('Valor ingresado NO corresponde a un  número...')

calculadora_basica()
