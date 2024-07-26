m = [
    [10, 2, 1, 7],
    [1, 5, 1, -8],
    [2, 3, 10, 6]   
]
numeroDeIteracoes = 50
erro = 0.05
valoresIniciais = [0.7, -1.6, 0.6]

def gaussJacobi(m, valoresIniciais, numeroDeIteracoes=0, erro=0):
    valoresAtualizados = valoresIniciais
    if (numeroDeIteracoes == 0 and erro == 0):
        print("Numero de iterações ou erro não informado")
        return
    
    if (numeroDeIteracoes != 0 and erro == 0):
        for i in range(numeroDeIteracoes):
            for x in range(len(valoresAtualizados)):
                valoresAtualizados[x] = calculaIteracao(m[x], x, valoresAtualizados)
            print(valoresAtualizados)
        return valoresAtualizados

    elif (numeroDeIteracoes == 0 and erro != 0):
        for _ in range(20000):

            ini = valoresAtualizados.copy()

            valoresNovos = [0 for x in range(len(valoresAtualizados))]
            for x in range(len(valoresAtualizados)):
                valoresNovos[x] = calculaIteracao(m[x], x, valoresAtualizados)
            valoresAtualizados = valoresNovos.copy()
            print("Valores de x para a iteração atual: ", valoresAtualizados)
            fim = valoresNovos
            erros = [abs(abs(fim[i]) - abs(ini[i])) for i in range(len(fim))]
            maxFim = max([abs(fim[x]) for x in range(len(fim))])
            maxErros = max(erros)
            print("Erro da iteração atual: ", maxErros/maxFim)
            if maxErros/maxFim < erro:
                print("Valores finais: ", valoresAtualizados)
                return valoresAtualizados

            # if (maximoInicial / maximoFinal) < erro:
            #     return valoresAtualizados

def calculaIteracao(linha, i, valoresIniciais):
    pivo = linha[i]
    resultadoLinha = linha[-1]
    resultado = 0
    for j in range(len(linha) - 1):
        if j == i:
            continue
        else:
            resultado -= linha[j] * valoresIniciais[j]
    resultado += resultadoLinha # O resultado da linha deve ser somado por ultimo por ser o unico valor que não troca de lado na equação ao se isolar os valores de x
    resultado = resultado / pivo
    return resultado
        
gaussJacobi(m, valoresIniciais, erro=erro)
# print(gaussJacobi(m, valoresIniciais, numeroDeIteracoes=numeroDeIteracoes))
