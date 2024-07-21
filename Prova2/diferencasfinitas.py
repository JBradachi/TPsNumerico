from math import factorial
#x = [-1, 0, 1]
#y = [4, 1, -1]
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 8, 27, 64, 125, 216, 343]
interpol = 1.5

def printTabela(tabela):
    for i in range(len(tabela[0])):
        for j in range((len(tabela))):
            if len(tabela[j]) > i:
                print(tabela[j][i], end=" "*(5 - len(str(tabela[j][i]))))
        print()
    print()
        
def calculaInterpol(tabela, interpol, x):
    resultado = tabela[0][0]
    z = (interpol - x[0])/(x[1]-x[0])
    for i in range(1, len(tabela)):
        aux1 = tabela[i][0]/factorial(i)
        aux2=1
        for j in range(i):
            aux2 = aux2*(z-j)
        resultado += aux1*aux2
    return resultado
                
            
def diferencasFinitas(x, y, interpol):
    tabela = list()
    tabela.append(y)
    for i in range(len(y)-1):
        delf = list()
        for j in range(len(tabela[i])-1):
            delf.append(tabela[i][j+1] - tabela[i][j])
        if delf[0] == 0: break
        tabela.append(delf)
    printTabela(tabela)
    resultado = calculaInterpol(tabela, interpol, x)
    return resultado

print(f"Valor {interpol} interpolado = {diferencasFinitas(x, y, interpol)}")
