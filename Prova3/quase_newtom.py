import numpy as np

# Função que implementa o método de Quase-Newton. O método recebe como parâmetros: 
# func = sistema de equações não lineares
# jac = jacobiano do sistema de equações não lineares
# x0 = valores iniciais
# err = erro máximo entre os valores de x de duas iterações consecutivas
# max_iter = número máximo de iterações

def quase_newton(func, jac, x0, err=1e-4, max_iter=100):

    # A primeira iteração é feita de forma diferente das demais, por isso está sendo feita separadamente. Uma das diferenças é o uso do jacobino original, e não dos B's aproximados.
    x_0 = np.array(x0, dtype=float)
    f_0 = np.array(func(x0)) # f é F(x^k)
    b_0 = jac(x_0)  # primeiro valor de B usando como base o jacobino
    s_0 = np.linalg.solve(b_0, -f_0) # encontrando o valor de s usando o B e o f
    print("=====================================")
    print("Iteracao: ", 0)
    print("-------------------------------------")
    print("F(x_k):\n", f_0)
    print("\nB(k)\n: ", b_0)
    # Calculando os novos valores de x e y
    x_1 = x_0 + s_0
    y_1 = np.array(func(x_1) - func(x_0))
    
    # Calcula os vetores s e y
    u_0 = (y_1 - b_0 @ s_0) / (np.transpose(s_0) @ s_0) # o operador @ realiza a multiplicação de matrizes
    a_0 = u_0 @ np.transpose(s_0) 
    b_1 = b_0 + a_0
    s_1 = np.linalg.solve(b_1, func(y_1))
    x_1 = x_0 + s_0

    # Renomeando x e f para a próxima iteração
    erro_atual = np.max(np.abs(x_0 - x_1))
    x_k = x_1
    f_k = y_1
    b_k = b_1

    print("\nRESULTADOS x_k: ", x_k)
    print("erro", erro_atual)

    # Critério de convergência
    if erro_atual < err:
        print(f"Convergência atingida em {k+1} iterações.")
        return x_k

    for k in range(max_iter):
        # Calcula a nova estimativa de x
        print("=====================================")
        print("Iteracao: ", k+1)
        print("-------------------------------------")
        print("F(x_k):\n", f_k)
        print("\nB(k)\n: ", b_k)
        f_k = np.array(func(x_k))
        s_k = np.linalg.solve(b_k, -f_k)

        # Calculando x_new e y_new 
        x_k_1 = x_k + s_k
        y_k = np.array(func(x_k_1)- f_k)

        # Calcula os vetores s e y
        u = (y_k - b_k @ s_0) / (np.transpose(s_k) @ s_k)


        a_k = u @ np.transpose(s_k) 
        b_k_1 = b_k + a_k

        # Atualiza x e f para a próxima iteração
        erro_atual = np.max(np.abs(x_k_1 - x_k))
        x_k = x_k_1
        b_k = b_k_1   

        print("\nRESULTADOS x_k: ", x_k)
        print("erro: ", erro_atual)

        
        # Critério de convergência
        if erro_atual < err:
            print(f"Convergência atingida em {k+1} iterações.")
            return x_k

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

x0 = [1, 5]  # Chute inicial
solucao = quase_newton(sistema_nao_linear, jacobiano, x0)
print(sistema_nao_linear(x0))
print("\n\n=====================================")
print("Solução encontrada:", solucao)
print("=====================================")