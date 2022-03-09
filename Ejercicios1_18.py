import math
from tkinter import Tk
from tkinter import messagebox


def ej1():
    op1 = 15.32
    op2 = 3

    print("suma: ", op1 + op2)
    print("resta: ", op1 - op2)
    print("multiplicación: ", op1 * op2)
    print("división: ", op1 / op2)
    print("módulo: ", op1 % op2)


def ej2():
    n = 5
    a = 9.43
    c = "45"
    print("n= %i, a= %f, c= %s" % (n, a, c))
    print("n+a = %f" % (n + a))
    print("a-n = %f" % (a - n))
    print("c = %i" % (int(c)))


def ej3():
    x = 2
    y = 9
    n = 10.5
    m = 2.75
    print("x= %i, y= %i, n= %f, m= %f" % (x, y, n, m))
    print("x + y = %i" % (x + y))
    print("x - y = %i" % (x - y))
    print("x * y = %i" % (x * y))
    print("x / y = %f" % (x / y))
    print('x mod y = %f' % (x % y))
    print("n + m = %f" % (n + m))
    print("n - m = %f" % (n - m))
    print("n * m = %f" % (n * m))
    print("n / m = %f" % (n / m))
    print("n mod m = %f" % (n % m))
    print("x*2 = %f" % (x * 2))
    print("y*2 = %f" % (y * 2))
    print("n*2 = %f" % (n * 2))
    print("m*2 = %f" % (m * 2))
    print("x+y+n+m =%f" % (x+y+n+m))
    print("x*y*n*m =%f" % (x * y * n * m))

def ej4():
    n=int(input("Introduzca un valor entero: "))
    result = n
    result += 77
    print("Incrementar N %i en 77 = %i" % (n, result))
    result -=3
    print("Decrementar N %i en 3 = %i" % (n, result))
    result = result * 2
    print("Duplicar N %i = %i" % (n, result ))



def ej5():
    a = 1
    b = 2
    c = 6
    d = 9

    x=b

    b = c
    c = a
    a = d
    d = x
    print ("a = %i, b = %i, c = %i, d = %i" % (a, b, c, d))

def ej6():
    op1 = 18
    op2 = 25

    if op1 > op2:
        print(str(op1) + " es mayor que " + str(op2))
    else:
        print(str(op2) + " es mayor que " + str(op1))

def ej7():
    minombre = "Esther"
    print("Te damos la bienvenida " + str(minombre))

def ej8():
    minombre = str(input("Introduzca su nombre: "))
    print("Te damos la bienvenida " + str(minombre))

def ej9():
    print("Se va a calcular el área de un círculo dado su radio.")
    radio = float(input("Por favor, introduzca el valor del radio: "))
    qpi = math.pi
    area = qpi*(math.pow(radio,2))
    print("El área es: " + str(area))

def ej10():
    print("Se va a indicar si el número introducido por teclado es divisible entre 2 o no")
    qnumero = float(input("Introduzca un número: "))
    if (qnumero % 2) == 0:
        print("El número " + str(qnumero) + " es divisible entre 2")
    else:
        print("El número " + str(qnumero) + " no es divisible entre 2")

def ej11():
    print("Se va a indicar el precio final con IVA(21%)")
    qprecio = float(input("Introduzca el precio:"))
    qpreciototal = qprecio + float(qprecio * 0.21)
    print("El precio final es: " + str(qpreciototal))

def ej12():
    while i<=100:
        if i>0:
            print(i)
        i += 1

def ej13():
    for i in range(101):
        print(i)

def ej14():
    i=1
    while i<=100:
        # if ((i % 2) == 0) & ((i % 3) == 0):
        if ((i % 6) == 0):
            print(i)
        i += 1

def ej15():
    nventas = (int(input("Introduzca el número total de ventas: ")))
    sumventas = 0
    for i in range(nventas):
        qventa = float(input("Venta " + str(i+1) + ": "))
        sumventas = float(sumventas) + float(qventa)
    print("El importe total de las " + str(nventas) + " ventas es: " + str(sumventas))


def ej16():

    qTipoDia = "no válido"
    qdia = str(input("Introduzca un día de la semana: "))

    if (qdia.upper() == "LUNES"):
        qTipoDia = "laboral"
    if (qdia.upper() == "MARTES"):
        qTipoDia = "laboral"
    if (qdia.upper() == "MIERCOLES") | (qdia.upper() == "MIÉRCOLES"):
        qTipoDia = "laboral"
    if qdia.upper() == "JUEVES":
        qTipoDia = "laboral"
    if qdia.upper() == "VIERNES":
        qTipoDia = "laboral"
    if (qdia.upper() == "SABADO") | (qdia.upper() == "SÁBADO"):
        qTipoDia = "no laboral"
    if qdia.upper() == "DOMINGO":
        qTipoDia = "no laboral"

    print("El día " + str(qdia) + " es " + qTipoDia)


def ej17():
    mipwd = "Pitufo"
    iTope = 3
    i = 0
    qpwd = ""

    while qpwd != mipwd:
        if i < iTope:
            i += 1
            qpwd = str(input("Introduzca contraseña: "))
        else:
            print("Contraseña incorrecta. Ha consumido los 3 intentos.")
            break
    if qpwd == mipwd:
        print("Enhorabuena")

def ej18():
#     CalculadoraInversa

    qsigno = ""

    op1 = int(input("Introduzca el primer operando: "))
    op2 = int(input("Introduzca el segundo operando: "))
    qsigno = str(input("Introduzca un signo aritmético: "))

    operadores = ('+', '-', '+', '/', '^', '%')

    qresultado = "nulo"
    if qsigno in operadores:
        qresultado = eval(str(op1) + str(qsigno) + str(op2))


    print("El resultado es: " + str(qresultado))
    root = Tk()
    root.withdraw()
    messagebox.showinfo(message="El resultado es: " + str(qresultado), title = "CalculadoraInversa")

def menu_principal():
    ejercicio = 0
    while (ejercicio < 1 or ejercicio > 18):
        ejercicio = int(input("Qué ejercicio desea ejecutar (1 - 18): "))

    if ejercicio == 1:
        ej1()
    if ejercicio == 2:
        ej2()
    if ejercicio == 3:
        ej3()
    if ejercicio == 4:
        ej4()
    if ejercicio == 5:
        ej5()
    if ejercicio == 6:
        ej6()
    if ejercicio == 7:
        ej7()
    if ejercicio == 8:
        ej8()
    if ejercicio == 9:
        ej9()
    if ejercicio == 10:
        ej10()
    if ejercicio == 11:
        ej11()
    if ejercicio == 12:
        ej12()
    if ejercicio == 13:
        ej13()
    if ejercicio == 14:
        ej14()
    if ejercicio == 15:
        ej15()
    if ejercicio == 16:
        ej16()
    if ejercicio == 17:
        ej17()
    if ejercicio == 18:
        ej18()
    print("El ejercicio %i ha finalizado", ejercicio)