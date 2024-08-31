import numpy as np

def broyden_method(func, jac, x0, err=1e-4, max_iter=10):
    """
    Método de Broyden para resolver sistemas de equações não lineares.

    Parâmetros:
    func: Função que define o sistema de equações não lineares (retorna vetor).
    x0: Vetor de chute inicial.
    tol: Tolerância para o critério de parada.
    max_iter: Número máximo de iterações.

    Retorna:
    x: Vetor solução aproximada.
    
    """

    x_0 = np.array(x0, dtype=float)
    f_0 = np.array(func(x0)) # f é F(x^k)
    b_0 = jac(x_0)  # Aproximação inicial do Jacobiano inverso B_m = B^k
    s_0 = np.linalg.solve(b_0, -f_0)
    print("B", b_0)
    print("solucao_linear" , s_0)

    # Calculando x_new e y_new 
    x_1 = x_0 + s_0
    y_1 = np.array(func(x_1) - func(x_0))
    
    # Calcula os vetores s e y
    # u_0 = np.outer((y_1 - b_0 @ s_0), s_0) / (np.transpose(s_0) @ s_0)
    u_0 = (y_1 - b_0 @ s_0) / (np.transpose(s_0) @ s_0)
    print("u", u_0)
    a_0 = u_0 @ np.transpose(s_0) 
    print("A", a_0)   
    b_1 = b_0 + a_0
    print("B", b_1)
    s_1 = np.linalg.solve(b_1, func(y_1))
    x_1 = x_0 + s_0

    print("Novos valores")
    print("x_1", x_1)
    print("y_1", y_1)
    print("B_m", b_1)

    # Renomeando x e f para a próxima iteração
    erro_atual = np.max(np.abs(x_0 - x_1))
    x_k = x_1
    f_k = y_1
    b_k = b_1
    print("erro", erro_atual)

    # Critério de convergência
    if erro_atual < err:
        print(f"Convergência atingida em {k+1} iterações.")
        return x_k

    for k in range(max_iter):
        # Calcula a nova estimativa de x
        print("=====================================")
        print("x_k",x_k)
        print("=====================================")
        f_k = np.array(func(x_k))
        s_k = np.linalg.solve(b_k, -f_k)

        # Calculando x_new e y_new 
        x_k_1 = x_k + s_k
        y_k = np.array(func(x_k_1)- f_k)

        # print("novos x =", x_k_1)
        
        # Calcula os vetores s e y
        u = (y_k - b_k @ s_0) / (np.transpose(s_k) @ s_k)
        # u = np.outer((y_k - b_k @ s_0), s_k) / (np.transpose(s_k) @ s_k)


        a_k = u @ np.transpose(s_k) 
        b_k_1 = b_k + a_k

        # s_k_1 = np.linalg.solve(b_k_1, func(y_k))
        # x_k_1 = x_k + s_k_1

        # Atualiza x e f para a próxima iteração
        erro_atual = np.max(np.abs(x_k_1 - x_k))
        print("erro", erro_atual)
        x_k = x_k_1
        b_k = b_k_1   
        print("x_k", x_k)
        print("b_k", b_k)


        
        # Critério de convergência
        if erro_atual < err:
            print(f"Convergência atingida em {k+1} iterações.")
            return x_k

    # raise ValueError("O método de Broyden não convergiu.")

# Exemplo de uso
def sistema_nao_linear(x):
    return np.array([
        x[0] + x[1] - 3,
        x[0]**2 + x[1]**2 - 9
    ])

def jacobiano(x):
    return np.array([
        [1, 1],
        [2 * x[0], 2 * x[1]]
    ])
# def sistema_nao_linear(x):
#     return [
#         x[0]**2 + x[1]**2 - 4,
#         x[0] - x[1] - 1
#     ]

# def jacobiano(x):
#     J = np.array([
#         [2 * x[0], 2 * x[1]],
#         [1, -1]
#     ])

x0 = [1, 5]  # Chute inicial
solucao = broyden_method(sistema_nao_linear, jacobiano, x0)
print(sistema_nao_linear(x0))
# print("Solução encontrada:", solucao)