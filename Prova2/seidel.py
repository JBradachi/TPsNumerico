#!/usr/bin/env python3

def main():
    n = 0
    equations = []
    print("=> Por favor, forneça a matriz aumentada do sistema linear:")
    while True:
        try:
            row = [float(s) for s in input().split()]
            if len(row) == 0: break
            equations.append(row)
            n += 1
        except EOFError:
            break
    if n == 0: return
    m = len(equations[0])
    k = int(input("=> Número de iterações de Gauss-Seidel: "))
    x = gauss_seidel(equations, n, m, k)
    print(f"=> Solução estimada: {x}")


# Aproxima a solução do sistema linear (dado na forma de uma matriz aumentada)
# através do método de Gauss-Seidel, utilizando um número fixo de iterações
def gauss_seidel(aug, n, m, k):
    x = [0 for _ in range(n)]
    for _ in range(k):
        for i in range(n):
            b = aug[i][-1]
            for j in range(m - 1):
                b -= (aug[i][j] * x[j]) if i != j else 0
            x[i] = b / aug[i][i]
    return x

if __name__ == "__main__":
    main()
