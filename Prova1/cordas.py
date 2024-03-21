#!/usr/bin/env python3
# cordas.py: estima raízes pelo método das cordas

def cordas(fn, x0, x1, epsi):
    "Aplica o método das cordas para estimar a raiz da função"
    # Estabelece um limite de iterações, evita loops infinitos
    n = 0
    MAX_ITERS = 1000
    while n < MAX_ITERS:
        # O método das secantes é exatamente como o método de Newton, mas
        # emprega uma aproximação para a derivada. Isso é particularmente
        # útil quando a forma analítica da função não é conhecida
        x = (x0 * fn(x1) - x1 * fn(x0)) / (fn(x1) - fn(x0))
        erro = abs(x - x1) / x1
        if erro < epsi:
            return x, erro  # precisão desejada foi alcançada
        # Do contrário, o processo continua com novos valores para x0 e x1
        x0, x1 = x1, x
        n += 1
    return x, erro  # limite de iterações atingido, retorna melhor aproximação


def aprox_sqrt(n):
    "Usa o método das cordas para estimar raízes quadradas"
    a, b = 1, 2
    # Isola a raiz em um bom intervalo [a,b]
    while not (a*a <= n <= b*b):
        a, b = b, a + 1
    # Talvez a raiz exata já tenha sido encontrada
    if n == a * a:
        return a, 0
    if n == b * b:
        return b, 0

    # Talvez não. Nesse caso, usamos o método das cordas
    def eqn(x):
        return x * x - n
    return cordas(eqn, a, b, 0.00000000000000000001)


def main():
    # Exemplo de aplicação: estima sqrt(5)
    aprox, erro = aprox_sqrt(5)
    print(f"Valor aproximado: {aprox} (erro: {erro})")
    from math import sqrt
    print(f"Valor exato: {sqrt(5)}")


if __name__ == "__main__":
    main()
