from math import floor

# Método de Runge-Kutta de quarta ordem. Recebe uma função func, valores
# iniciais x0 e y0, um valor de x e um passo h. Aproxima a função f(x),
# onde f'(x) = func(x, y) e f(x0) = y0
def rk4(func, x0, y0, x, h):
    y = y0
    n = floor((x - x0) / h) # número de iterações depende do passo
    for i in range(n):
        k1 = h * func(x0, y)
        k2 = h * func(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * func(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * func(x0 + h, y + k3)
        # Estima o próximo valor de y com os valores k
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        x0 += h
    return y

if __name__ == "__main__":
    dydx = lambda x, y : (x - y) / 2
    print("Seja y' = (x - y) / 2, com x0 = 0 e y0 = 1")
    x = float(input("Valor de x para o qual deseja-se aproximar y(x):  "))
    h = float(input("Passo h: "))
    y = rk4(dydx, 0, 1, x, h)
    print(f"\n=> Resposta aproximada: {y}")
