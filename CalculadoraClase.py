
opcion=1

while(opcion<=3):

    print("===CALCULADORA===")
    print("Elige una opcion")
    print("1-Suma")
    print("2-Resta")
    print("3-Salir")

    opcion1 = int(input("Escribe tu elección:"))

    if(opcion1==1):
        a=float(input("Introduce el primer numero\n"))
        b=float(input("Introduce el segundo numero\n"))
        resultado= a+b
        print("El resultado de la suma es:",resultado)
    elif(opcion1==2):
        a=float(input("Introduce el primer numero\n"))
        b=float(input("Introduce el segundo numero\n"))
        resultado= a-b
        print("El resultado de la resta es:",resultado)
    elif(opcion1==3):
        break
    else:
        print("NUMERO INVALIDO")

    opcion=opcion+1
