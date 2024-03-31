#!/usr/bin/env python3
# pegaso.py: estima raízes pelo método de Pégaso


def pegaso(fn, a, b, prec):
    # n é um contador que registra o número de iterações (assim limitando um loop infinito)
    n = 0
    MAX_ITERS = 1000

    # No método Pégaso, a ideia principal é, a cada iteração, calcular novos limites para o intervalo (assim como em outros métodos). Porém, diferente dos outros métodos, o Pégaso não atualiza somente os valores dos limites do intervalo, mas também os valores da função nos limites do intervalo. Dessa forma, ele se torna mais rápido e otimizado.
    # Em vista disso, foram criadas as variáveis Fa e Fb para armazenar os valores da função nos limites do intervalo.

    Fa = fn(a)
    Fb = fn(b)

    while n < MAX_ITERS:
        n += 1
        

        x = b - ((Fb*(b-a))/(Fb-Fa)) # Encontra novo valor
        erro = abs(b - a) / a # Calcula o erro

        if erro < prec:
            return x, n # Caso o erro seja menor que a precisão, retorna a raiz aproximada
        
        # Caso o valor de f(x) e f(b) tenham sinais diferentes, o valor exato encontra-se em algum ponto entre eles, portanto atualiza-se os intervalos
        # print(f"a: {a} b: {b} x: {x}")
        # print(f"Fa: {Fa} Fb: {Fb} fn(x): {fn(x)}")
        if (fn(x) * Fb) < 0: 
            a = b
            Fa = Fb
            b = x
            Fb = fn(x)
        
        # Caso contrário, atualiza-se o valor de f(a) de forma a otimizar os calculos
        elif (fn(x)*Fb) > 0:
            b = x
            Fb = fn(x)
            Fa = fn(a)*fn(b)/(fn(x)+fn(b))
            
    return x, n  # como o limite de iterações foi atingido, retorna a melhor aproximação
