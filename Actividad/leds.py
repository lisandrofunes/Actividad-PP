#2 , 3 y 5 = 5 
#1 = 2 
#4 = 4
#7 = 3
#8 = 9
#0 , 9 y  6 = 6
i = 0;
aux = 1
press = ""
while (aux < 2001 ):
    cont = 0;
    N = input("ingrese una secuencia de numeros\n")
    for i in range(len(N)):
        if N[i] == "1":
            cont = cont + 2
        elif (N[i] == ("2")) or (N[i] == ("3")) or (N[i] == ("5")):
            cont = cont + 5
        elif N[i] == "4":
            cont = cont + 4
        elif N[i] == "7":
            cont = cont + 3
        elif N[i] == "8":
            cont = cont + 9
        elif (N[i] == "6") or (N[i] == "9") or (N[i] == "0"):
            cont = cont + 6;
    print("CASO DE PUEBA\n", aux, "\nCantidad de LEDS usados\n" , cont)
    press = input("Presione x para salir y ENTER para continuar\n")
    aux = aux + 1
    if press == "x":
        break  
