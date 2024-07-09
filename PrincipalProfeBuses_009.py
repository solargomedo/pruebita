import numpy as np
import funcionesBuses as fun
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
        fun.mostrarMatriz(bus)
    if opc==2:
        fun.ingresar(bus, pasajeros)
    if opc==3:
        fun.mostrarMatriz(pasajeros)
    if opc==4:
        totalRecaudado = fun.totalizar(bus)
        print(f"Total Recaudado: {totalRecaudado}")
    if opc==5:        
        break

