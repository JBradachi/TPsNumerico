#!/usr/bin/env python3
# newton.py: estima as raízes das funções pelo método de newton

def newton(fn, dfn, x0, erro):
    """
    Aplica o método de Newton para aproximar raízes de funções
    Retorna a raiz aproximada e o número de iterações
    """
    if dfn == 0:
        print("Erro, não é possível usar o método")
        return 0
    MAX_ITERS = 1000
    n = 0
    x = 0
    xn = 0
    while n < MAX_ITERS and erro < abs(x0-x):
        print(f"n={n}, xn={x}, x0={x0}, fn={fn(x)}, erro={abs(x0 - x)}")
        xn = x0 - (fn(x0) / dfn(x0))
        x = x0
        x0 = xn
        n += 1
    return x, n
