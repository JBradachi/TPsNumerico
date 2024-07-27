#!/usr/bin/env python3

# A partir de uma matriz quadrada A, encontra uma matriz triangular inferior
# unidiagonal L e uma matriz triangular superior U tal que A = LU. Assume que
# a matriz A pode ser decomposta dessa maneira (i.e. não verifica as condições
# necessárias)
def lu_decompose(matrix, n):
    lower = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
    upper = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        # Triangular superior (U)
        for k in range(i, n):
            # Somatório de L_ij * U_jk
            acc = 0
            for j in range(i):
                acc += lower[i][j] * upper[j][k]
            # Definindo U_ik
            upper[i][k] = matrix[i][k] - acc
        # Triangular inferior unidiagonal (L)
        for k in range(i, n):
            if i == k: continue # já inicializado
            # Somatório de L_kj * U_ji
            acc = 0
            for j in range(i):
                acc += lower[k][j] * upper[j][i]
            # Definindo L_ki
            lower[k][i] = (matrix[k][i] - acc) / upper[i][i]
    return lower, upper

# Resolve o sistema dado pela matrix aumentada A|B por meio da fatoração LU.
# Assume que o sistema tem n equações e n incógnitas, ou seja, A|B tem dimensões
# Nx(N + 1)
def lu_solve(aug, n):
    b = []
    a = [list() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[i].append(aug[i][j])
        b.append(aug[i][-1])
    lower, upper = lu_decompose(a, n)

    # Resolve o sistema Ly = B
    y = [b[i] for i in range(n)]
    for i in range(n):
        for j in range(i):
            y[i] -= lower[i][j] * y[j]
    # Resolve o sistema Ux = y
    x = [y[i] for i in range(n)]
    for i in range(n - 1, -1, -1): # itera as linhas ao contrário
        for j in range(i + 1, n):
            x[i] -= upper[i][j] * x[j]
        x[i] /= upper[i][i]
    return x

def main():
    n = 0
    equations = []
    print("=> Por favor, forneça a matriz aumentada do sistema linear:")
    print("(NOTA: número de equações e incógnitas deve ser igual)")
    while True:
        try:
            row = [float(s) for s in input().split()]
            if len(row) == 0: break
            equations.append(row)
            n += 1
        except EOFError:
            break
    if n == 0: return
    x = lu_solve(equations, n)
    print(f"=> Solução exata do sistema: {x}")


if __name__ == "__main__":
    main()
