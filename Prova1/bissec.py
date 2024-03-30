#!/usr/bin/env python3
# bissec.py: estima raízes pelo método da bissecção

<<<<<<< HEAD
"""
    Aplica o método da bisecção para estimar a raiz da função
    NOTA: fn(a) * fn(b) < 0 é assumido como condição inicial!
    Retorna a raiz aproximada e o número de iterações
"""

def bissec(fn, a, b, prec):
=======
def bissec(fn, a, b, prec):
    """
    Aplica o método da bisecção para estimar a raiz da função
    NOTA: fn(a) * fn(b) < 0 é assumido como condição inicial!
    Retorna a raiz aproximada e o número de iterações
    """
>>>>>>> 42b1723f1f7f2e702f3986f55f2a9557ae39300a
    # Estabelece um limite de iterações, evita loops infinitos
    n = 0
    MAX_ITERS = 1000
    x0 = (a + b) / 2  # estimativa inicial
    while n < MAX_ITERS:
        n += 1
        # As estimativas da raiz são dadas simplesmente pelo ponto médio do
        # intervalo (a,b). A cada iteração, esse intervalo é divido na metade
        # e o processo de repete, até que se atinja a precisão desejada
        sinal = fn(a) * fn(x0)
        a, b = (a, x0) if sinal < 0 else (x0, b)
        x = (a + b) / 2  # nova estimativa
        # Cálculo do erro e teste de precisão
        erro = abs(x - x0) / x0
<<<<<<< HEAD
        print("n=", n, "xn=", x, "a=", a, "b=", b, "fn=", (fn(x)) , "erro=", erro)
        if erro < prec:
            return x, erro  # precisão desejada foi obtida
=======
        if erro < prec:
            return x, n  # precisão desejada foi obtida
>>>>>>> 42b1723f1f7f2e702f3986f55f2a9557ae39300a
        # Do contrário, o processo continua
        x0 = x
    return x, n  # limite de iterações atingido, retorna melhor aproximação
