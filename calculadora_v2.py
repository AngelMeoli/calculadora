import psycopg2

try:
    conexion=psycopg2.connect(
        host ="localhost",
        port = "5432",
        user = "postgres",
        password = "angel",
        dbname = "tarea6"
    )
    print("CONEXION EXITOSA")
except psycopg2.Error as e:
    print("HUBOUN ERROR EN LA CONEXION")

try:
    menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. VER DATOS \n 8. SALIR \n" ))
except ValueError:
    print("Tipo de dato no valido!!")
    menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. VER DATOS \n 8. SALIR \n" ))

def suma():
    print("----------------Selecciono Suma----------------- \n")

    try:
        cursor= conexion.cursor()
        operacion="suma"
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        resultado = a + b
        cursor.execute("INSERT INTO calculadora VALUES(%s,%s,%s,%s);",(operacion,a,b,resultado))
        conexion.commit()
        cursor.close()
        
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("---------------El resultado es: ",resultado)

def resta():
    print("--------------Selecciono Resta--------------- \n")
 
    try:
        cursor= conexion.cursor()
        operacion="resta"
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        resultado = a - b
        cursor.execute("INSERT INTO calculadora VALUES(%s,%s,%s,%s);",(operacion,a,b,resultado))
        conexion.commit()
        cursor.close()
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",resultado)

def multiplicacion():
    print("------------Selecciono Multiplicacion------------- \n")

    try:
        cursor= conexion.cursor()
        operacion="multiplicacion"
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        resultado = a * b
        cursor.execute("INSERT INTO calculadora VALUES(%s,%s,%s,%s);",(operacion,a,b,resultado))
        conexion.commit()
        cursor.close()
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",resultado)

def division():
    print("-------------Selecciono Division-------------- \n")
    
    try:
        cursor= conexion.cursor()
        operacion="division"
        a=int(input("Ingrese dividendo: "))
        b=int(input("Ingrese divisor: "))
        resultado = a/b
        cursor.execute("INSERT INTO calculadora VALUES(%s,%s,%s,%s);",(operacion,a,b,resultado))
        conexion.commit()
        cursor.close()
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("El resultado es: ",resultado)

def potencia():
    print("--------------Selecciono Potencia--------------- \n")
    
    try:
        cursor= conexion.cursor()
        operacion="potencia"
        a=int(input("Ingrese la base: "))
        b=int(input("Ingrese el exponente: "))
        resultado = a**b
        cursor.execute("INSERT INTO calculadora VALUES(%s,%s,%s,%s);",(operacion,a,b,resultado))
        conexion.commit()
        cursor.close()
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",resultado)

def raiz():
    print("--------------Selecciono Raiz--------------- \n")
    
    try:
        cursor= conexion.cursor()
        operacion="raiz"
        a=int(input("Ingrese la base: "))
        b=int(input("Ingrese la raiz: "))
        resultado = a**(1/b)
        cursor.execute("INSERT INTO calculadora VALUES(%s,%s,%s,%s);",(operacion,a,b,resultado))
        conexion.commit()
        cursor.close()
    except ZeroDivisionError:
        print('¡No se puede dividir por cero!')
    except ValueError:
        print("Tipo de dato no admitido!")
    else:
        print("------------El resultado es: ",resultado)

def verdatos():
    print("--------------Selecciono Ver Datos--------------- \n")
    cursor= conexion.cursor()
    SQL = "SELECT*FROM calculadora;"
    cursor.execute(SQL)
    valores=cursor.fetchall()
    print(valores)
    cursor.close()

while menu !=8:

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
    elif menu==7:
        verdatos()
    else:
        print("Opcion no valida!!")    

    try:
        menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. VER DATOS \n 8. SALIR \n" ))      
    except ValueError:
        print("Tipo de dato no admitido!")
        menu = int(input("------------ SELECCIONE LA OPERACION----------------- \n 1. SUMA \n 2. RESTA \n 3. MULTIPLICACION \n 4. DIVISION \n 5. POTENCIA \n 6. RAIZ \n 7. VER DATOS \n 8. SALIR \n" ))
conexion.close()

def ingresardatos():
    cursor= conexion.cursor()
    operacion=str(input("ingrese la operacion: "))
    valor1=int(input("Ingrese el primer numero: "))
    valor2=int(input("Ingrese el segundo numero: "))
    resultado=valor1-valor2
    cursor.execute("INSERT INTO calculadora VALUES(%s,%s,%s,%s);",(operacion,valor1,valor2,resultado))
    conexion.commit()
    cursor.close()
    conexion.close()


    



