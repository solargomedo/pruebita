
def mostrarMatriz(  mRecibida  ):
    for i in range(10):
            print(f"Fila{i+1}: {mRecibida[i,0]}\t{mRecibida[i,1]}\t{mRecibida[i,2]}\t{mRecibida[i,3]}")

def ingresar( dis , pas ):
    fila = int(input("ingrese la fila del bus:"))
    columna=int(input("ingrese la columna del bus:"))
    dis[fila,columna]="X"
    nombre=input("ingrese el nombre del pasajero:")
    pas[fila,columna]=nombre

def totalizar(mat):
    contador=0
    for i in range(10):
        for j in range(4):
            if (mat[i,j]=="X"):
                contador = contador + 1
    total = contador*15000 
    return total

def buscar(mat,valorBuscado):
    res=False
    for i in range(10):
          for j in range(4):
               if mat[i,j]==valorBuscado:
                 res = True
                 break
    return res