x = [-1, 0, 1, 2]
y = [7, 4, 1, 4]
interpol = 1.5

def lagrange(x, y, interpol):
    resultado = 0
    for i in range(len(x)):
        aux = 1
        for j in range(len(x)):
            if i == j: continue
            aux = aux*((interpol-x[j])/(x[i]-x[j]))
        resultado += aux*y[i]
    return resultado

print(lagrange(x, y, interpol))
