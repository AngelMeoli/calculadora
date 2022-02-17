
try:
    menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. SALIR \n" ))
except ValueError:
    print("Tipo de dato no valido!!")
    menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. SALIR \n" ))


def suma():
    print("----------------Selecciono Suma----------------- \n")

    try:
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        result = a + b
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("---------------El resultado es: ",result)

def resta():
    print("--------------Selecciono Resta--------------- \n")
 
    try:
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        result = a - b
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",result)

def multiplicacion():
    print("------------Selecciono Multiplicacion------------- \n")

    try:
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        result = a * b
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",result)

def division():
    print("Selecciono Division \n")
    
    try:
        a=int(input("Ingrese el dividendo: "))
        b=int(input("Ingrese el divisor: "))
        result = a / b
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("El resultado es: ",result)

def potencia():
    print("--------------Selecciono Potencia--------------- \n")
    
    try:
        a=int(input("Ingrese la base: "))
        b=int(input("Ingrese la potencia: "))
        result = a**b
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",result)

def raiz():
    print("--------------Selecciono Raiz--------------- \n")
    
    try:
        a=int(input("Ingrese la base: "))
        b=int(input("Ingrese la raiz: "))
        result = a**(1/b)
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",result)
      

while menu !=7:

    if menu ==1:
        suma()
            
    elif menu==2:
        resta()
    elif menu==3:
        multiplicacion()
    elif menu==4:
        division()
    elif menu==5:
        potencia()
    elif menu==6:
        raiz()
    else:
        print("Opcion no valida!!")    

    try:
        menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. SALIR \n" )) 
      
    except ValueError:
        print("Tipo de dato no admitido!")
        menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. SALIR \n" )) 



    


