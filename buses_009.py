import numpy as np
bus = np.empty([10,4], dtype='object')
pasajeros = np.empty([10,4], dtype='object')
conta=0
for i in range(10):
    for j in range(4):
        conta = conta+1
        bus[i,j]=conta

while(True):
    print("MENU BUSES")
    print("1.- Ver disponibilidad")
    print("2.- Reservar")
    print("3.- Ver Nomina pasajeros")
    print("4.- Totalizar bus")
    print("5.- Salir")
    opc = int(input("ingrese su opcion 1-5"))
    if opc==1:
        for i in range(10):
            print(f"Fila{i+1}: {bus[i,0]}\t{bus[i,1]}\t{bus[i,2]}\t{bus[i,3]}")
    if opc==2:
        fila = int(input("ingrese la fila del bus:"))
        columna=int(input("ingrese la columna del bus:"))
        bus[fila,columna]="X"
        nombre=input("ingrese el nombre del pasajero:")
        pasajeros[fila,columna]=nombre
    if opc==3:
        print(pasajeros)
    if opc==4:
        contador=0
        for i in range(10):
            for j in range(4):
                if (bus[i,j]=="X"):
                    contador = contador + 1
        total = contador*15000
        print(f"Total Recaudado: {total}")
    if opc==5:        
        break

