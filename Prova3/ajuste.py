import numpy as np

def ajuste_quadratico(x, y):
    # Construir a matriz de design A com colunas x^2, x e 1
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    
    # Resolver o sistema de equações normais A.T @ A @ coef = A.T @ y
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    
    # Definir a função quadrática ajustada
    def funcao_ajustada(x):
        return coef[0] * x**2 + coef[1] * x + coef[2]
    
    return funcao_ajustada, coef

# Exemplo de uso:
x = np.array([-1, 0, 1, 2])
y = np.array([0, -1, 0, 7])

funcao_ajustada, coeficientes = ajuste_quadratico(x, y)
print("Coeficientes: a =", coeficientes[0], ", b =", coeficientes[1], ", c =", coeficientes[2])

# Testando a função ajustada
print("f(6) =", funcao_ajustada(0))