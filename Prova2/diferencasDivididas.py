#Exemplo do livro:
x = [0.0, 0.1, 0.3, 0.6, 1]
y = [1.000, 2.001, 4.081, 8.296, 21.00]
xProcurado = 0.2

# Outro exemplo
# x = [0.0, 0.2, 0.3, 0.5, 0.6]
# y = [1.008, 1.064, 1.125, 1.343, 1.512]
# xProcurado = 0.4

# Para facilitar o código, a matriz é calculada de cima para baixo, e não da esquerda pra direita
def diferencasDivididas(x,y, xProcurado):
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
    print('Matriz de diferenças divididas:')
    printaMatriz(m)
    coeficientes = [m[i][0] for i in range(1,len(x)+1)]
    resultado = calculaInterpolacao(coeficientes, x, y, xProcurado)
    print('Resultado: ', resultado )
    return resultado

# Para cada celula da matriz de diferenças divididas, cacula o valor naquela posição
def calculaDiferenca(i, j, m):
    m[i][j] = (m[i-1][j+1] - m[i-1][j]) / (m[0][j+i-1] - m[0][j]) 

def printaMatriz(m):
    for i in range(len(m)):
        print(m[i]) 
    print('\n')

# Calcula a interpolação com base nos coeficientes calculados
def calculaInterpolacao(coeficientes, x, y, xProcurado):
    tot = 0
    for i in range(len(coeficientes)):
        produto = 1
        for j in range(i):
            print(j)
            produto *= (xProcurado - x[j])

        tot += coeficientes[i]*(produto)
    return tot

diferencasDivididas(x,y,xProcurado)