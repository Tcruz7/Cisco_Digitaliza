import os


def menu():
    os.system('clear')
    # ejeculta comando para lipiar la patalla.
    print("\nQue operación deseas realizar?: ")
    print("")
    print("1 - Somar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Pontencializar")
    print("6 - Salir")
    print("")
while True:
    # mostramos el metodo definido como menu.
    menu()

    #Definimos el metodo que realiza la suma!
    def Sumar():
        a = int(input("Digite el primer sumado: "))
        b = int(input("Digite el segundo sumado: "))
        c = int(a + b)
        print("La suma de " + str(a) + " y " + str(b) + " es: " + str(c) + "\n")

#Definimos el metodo que realiza la resta!
    def Restar():
        a = int(input("Digite el minuendo: "))
        b = int(input("Digite el sustraendo: "))
        c = int(a - b)
        print("La Resta entre " + str(a) + " y " + str(b) + " es: " + str(c) + "\n")

#Definimos el metodo que realiza la multiplicacion!
    def Multiplicar():
        a = int(input("Digite el multiplicando: "))
        b = int(input("Digite el multiplicador: "))
        c = int(a * b)
        print("La multiplicacion de " + str(a) + " por " + str(b) + " es: " + str(c) + "\n")

#Definimos el metodo que realiza la division!
    def Dividir():
        a = int(input("Digite el dividendo: "))
        b = int(input("Digite el divisor: "))
        c = float(a / b)
        print("La division de " + str(a) + " por " + str(b) + " es: " + str(c) + "\n")

#Definimos el metodo que realiza la potencia!
    def pPow():
        base = int(input("Digite el numero: "))
        exponente = int(input("Digite el exponente: "))
        resultado = base
        for x in range(exponente - 1): resultado *= base
        print("\n" + str(base) + " elevado a  " + str(exponente) + ": " + str(resultado))


    opicionMenu = input("Digite aqui >> ")

    if str(opicionMenu) == "1":

        print("\n Has elegido hacer una suma \n")
        Sumar()


    elif opicionMenu == "2":
        print("\n Has elegido hacer una Resta \n")
        Restar()

    elif opicionMenu == "3":
        print("\n Has elegido hacer una Multiplicación \n")
        Multiplicar()

    elif opicionMenu == "4":
        print("\n Has elegido hacer una Divivion \n")
        Dividir()

    elif opicionMenu == "5":
        print("\n Has elegido Potencializar \n")
        pPow()

    elif opicionMenu == "6":
        print("\n Terminamos a pedido del usuario! \n")
        print("==== Que tengas un buen dia! ====")
        break
    else:
        print("")
        print("No has selecionado ningun valaor!!! \n")
