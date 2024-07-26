x = [0.3, 1.5, 2.1]
y = [3.09, 17.25, 25.41]

def diferencasDivididas(x,y):
    if len(x) != len(y):
        print('O numero de entradas para x é diferente que o número de entradas de y')
        return
    m = [[0 for i in range(len(x))] for j in range(len(x)+1)]
    for i in range(len(y)):
        m[0][i] = x[i]
        m[1][i] = y[i]
    for i in range(2,len(x)+1):
        for j in range(len(x)+1-i):
            print(i,j)
            calculaDiferenca(i, j, m)
            printaMatriz(m)

def calculaDiferenca(i, j, m):
    m[i][j] = (m[i-1][j+1] - m[i-1][j]) / (m[0][j+i-1] - m[0][j]) 

# def printaMatriz(m):
#     for i in range(len(m)):
#         print(m[i]) 
#     print('\n')



diferencasDivididas(x,y)
"""
[0.3, 1.5, 2.1]
[3.09, 17.25, 25.41]
[11.38, 13.60, 0]
[1.0, 0, 0]

[
[1,2,3,4,5,6],0
[0,0,0,0,0,0],2
[0,0,0,0,0,0],3
[0,0,0,0,0,0],4
[0,0,0,0,0,0],5
[0,0,0,0,0,0],6
]




"""