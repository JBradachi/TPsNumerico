#!/usr/bin/env python3
# cordas.py: estima raízes pelo método das cordas

# NOTA é usada aqui uma pequena variação do método das cordas em relação ao que
# O Lúcio passou na aula. Essa forma não assume nenhum ponto fixo, sendo
# portanto semelhante ao método Pégaso, mas sem o artíficio mais sofisticado
# que o Pégaso emprega com testes de sinal e etc.
def cordas(fn, x0, x1, prec):
    """
    Aplica o método das cordas para estimar a raiz da função
    Retorna a raiz aproximada e o número de iterações
    """
    # Estabelece um limite de iterações, evita loops infinitos
    n = 0
    MAX_ITERS = 1000
    while n < MAX_ITERS:
        n += 1
        # O método das secantes é exatamente como o método de Newton, mas
        # emprega uma aproximação para a derivada. Isso é particularmente
        # útil quando a forma analítica da função não é conhecida
        x = (x0 * fn(x1) - x1 * fn(x0)) / (fn(x1) - fn(x0))
        erro = abs(x - x1) / x1
        if erro < prec:
            return x, n  # precisão desejada foi alcançada
        # Do contrário, o processo continua com novos valores para x0 e x1
        x0, x1 = x1, x
    return x, n  # limite de iterações atingido, retorna melhor aproximação
