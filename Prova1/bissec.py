#!/usr/bin/env python3
# bissec.py: estima raízes pelo método da bissecção

"""
    Aplica o método da bisecção para estimar a raiz da função
    NOTA: fn(a) * fn(b) < 0 é assumido como condição inicial!
    Retorna a raiz aproximada e o número de iterações
"""

def bissec(fn, a, b, prec):
    # Estabelece um limite de iterações, evita loops infinitos
    n = 0
    MAX_ITERS = 1000
    x0 = (a + b) / 2  # estimativa inicial
    while n < MAX_ITERS:
        # As estimativas da raiz são dadas simplesmente pelo ponto médio do
        # intervalo (a,b). A cada iteração, esse intervalo é divido na metade
        # e o processo de repete, até que se atinja a precisão desejada
        sinal = fn(a) * fn(x0)
        a, b = (a, x0) if sinal < 0 else (x0, b)
        x = (a + b) / 2  # nova estimativa
        # Cálculo do erro e teste de precisão
        erro = abs(x - x0) / x0
        print("n=", n, "xn=", x, "a=", a, "b=", b, "fn=", (fn(x)) , "erro=", erro)
        if erro < prec:
            return x, erro  # precisão desejada foi obtida
        # Do contrário, o processo continua
        x0 = x
        n += 1
    return x, erro  # limite de iterações atingido, retorna melhor aproximação


def main():
    # Exemploe de aplicação: estima sqrt(5)
    def f(x):
        return x * x - 5
    res, err = bissec(f, 2, 3, 0.000000000000001)
    print(f"Aproximação: {res} (erro = {err})")
    from math import sqrt
    print(f"Valor exato: {sqrt(5)}")


if __name__ == "__main__":
    main()
