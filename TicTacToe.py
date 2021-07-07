import random
import time
#------------------------------------------------------------VARIABLES------------------------------------------------------------------------
cruz='\033[91m'+'\033[1m'+'X'+'\033[0m'
circulo='\033[94m'+'\033[1m'+'O'+'\033[0m'

tablero=[[1,2,3],
         [4,cruz,6],
         [7,8,9]]
#------------------------------------------------------------FUNCIONES------------------------------------------------------------------------
def ImprimirTablero(tablero):
    print(f"""
    +-------+-------+-------+
    |       |       |       |
    |   {tablero[0][0]}   |   {tablero[0][1]}   |   {tablero[0][2]}   |
    |       |       |   ]    |
    +-------+-------+-------+
    |       |       |       |
    |   {tablero[1][0]}   |   {tablero[1][1]}   |   {tablero[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {tablero[2][0]}   |   {tablero[2][1]}   |   {tablero[2][2]}   |
    |       |       |       |
    +-------+-------+-------+""")



def Posicion(numero,tablero):
    fila=-1
    columna=-1
    
    for i in tablero:
        if numero in i:
            fila=tablero.index(i)
            columna=tablero[fila].index(numero)
    
    return fila,columna

def EsLibre(pos):
    if pos!=(-1,-1):
        return True
    else:
        return False

def Movimiento(simbolo,numero,tablero):

    fila,columna=Posicion(numero,tablero)         
    tablero[fila][columna]=simbolo

def GanarPorFila(tablero):
    

    for fila in tablero:
        
        tres_en_raya=True

        for columna in range(len(fila)):
            simbolo=fila[0]
            if fila[columna]!=simbolo:
                tres_en_raya=False
                break

        if tres_en_raya:
            
            return True

def GanarPorColumna(tablero):

    for columna in range(len(tablero)):
        
        simbolo=tablero[0][columna]
        tres_en_raya=True

        for fila in range(len(tablero)):
            if tablero[fila][columna]!=simbolo:
                tres_en_raya=False
                break
        if tres_en_raya:
            return True

def GanarPorDiagonalFacil(tablero):
    simbolo=tablero[0][0]
    tres_en_raya=True

    for i in range(len(tablero)):
        if tablero[i][i]!=simbolo:
            tres_en_raya=False
            break
    if tres_en_raya:
        return True

def GanarPorDiagonalAlterna(tablero):
    simbolo=tablero[0][2]
    tres_en_raya=True
    
    for i in range(len(tablero)):
        if tablero[i][-i-1]!=simbolo:
            tres_en_raya=False
            break
    if tres_en_raya:
        return True

def Gana():
    return GanarPorFila(tablero) or GanarPorColumna(tablero) or GanarPorDiagonalFacil(tablero) or GanarPorDiagonalAlterna(tablero)

#-----------------------------------------------------------------JUEGO----------------------------------------------------------------------

count=1
ImprimirTablero(tablero)

while count<9:
    
    movUser=int(input('Ingrese movimiento: '))
    fila,columna=Posicion(movUser,tablero)

    while not EsLibre((fila,columna)):
        movUser=int(input('Ingrese movimiento: '))
        fila,columna=Posicion(movUser,tablero)
        
    Movimiento(circulo,movUser,tablero)
    
    ImprimirTablero(tablero)

    if Gana():
        print('Ha Ganado, Felicidades')
        break

    movBot=random.randint(1,9)
    fila,columna=Posicion(movUser,tablero)
    
    while not EsLibre((fila,columna)):
        movBot=random.randint(1,9)
        fila,columna=Posicion(movBot,tablero)

    Movimiento(cruz,movBot,tablero)
    
    print(f'La PC jugara en la posicion {movBot}')
    time.sleep(1.0)
    ImprimirTablero(tablero)

    if Gana():
        print('Ha Ganado la PC')
        break

    count+=2

else:
    print('Empate')




    










