print "Calculadora"
print "1.- Suma"
print "2.- Resta"
print "3.- Multiplicacion"
print "4.- Division"
print "5.- Potencia"
No_operacion= input("Ingrese numero de Operacion: ")
if No_operacion == 1:
    print "Eligio la operacion Suma"
elif No_operacion == 2:
    print "Eligio la operacion Resta"
elif No_operacion == 3:
    print "Eligio la operacion Multiplicacion"
elif No_operacion == 4:
    print "Eligio la operacion Division"
elif No_operacion == 5:
    print "Eligio la operacion Potencia"
else:
    print "El Numero que eligio No esta disponible"
if No_operacion == 1:
    def suma():
        Numerosuma1= input("ingrese primer numero para sumar")
        Numerosuma2= input("ingrese sgundo numero para sumar")
        print Numerosuma1 + Numerosuma2
    suma()
if No_operacion == 2:
    def resta():
        Numerorestar1= input("ingrese primer numero para restar")
        Numerorestar2= input("ingrese sgundo numero para restar")
        print Numeroresta1 - Numeroresta2
    resta()
if No_operacion == 3:
    def multiplicacion():
        Numeromulti1= input("ingrese primer numero para Multiplicar")
        Numeromulti2= input("ingrese sgundo numero para Multiplicar")
        print Numerosuma1 * Numerosuma2
    multiplicacion()
if No_operacion == 4:
    def division():
        Numerodivi1= input("ingrese primer numero para Dividir")
        Numerodivi2= input("ingrese sgundo numero para Dividir")
        print Numerodivi1 / Numerodivi2
    division()
if No_operacion == 5:
    def potencia():
        Numeropote1= input("ingrese primer numero para potenciar")
        print Numeropote1 * srt(2)
    potencia()