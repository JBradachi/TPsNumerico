#!/usr/bin/env python3
# main.py: script principal que usa os métodos definidos em outros arquivos
# para computar certos valores comuns, possibilitanto dessa forma testar
# e comparar os métodos

def main():
    import bissec, cordas, newton, iter_linear, math, pegaso
    from sys import exit

    print("======= Máquina de aproximação de raiz quadrada =======")
    n = int(input("Digite um número: "))
    print("Escolha o método a ser usado: ")
    print("1. Bissecção")
    print("2. Cordas (secantes)")
    print("3. Newton")
    print("4. Interação Linear (usa a equação x³ - x - 1)")
    print("5. Pegaso")
    op = int(input("Índice do método: "))

    # Isola a raiz em um intervalo
    a, b = 1, 2
    while not (a * a <= n <= b * b):
        a, b = b, a + 1

    def eqn(x):
        "Equação simples para a aproximação"
        return x * x - n
    prec = 0.000000000000001

    # Exemplo de aplicação x^3-x-1
    def eqIntL(x):
        return (math.pow(x, 3)) - x - 1
    # F(x) Obtida isolando x^3  ((x+1)^(1/3))
    def FeqIntL(x):
       return math.pow((x+1), 1/3)
    match op:
        case 1:
            sqrt_n, iters = bissec.bissec(eqn, a, b, prec)
        case 2:
            sqrt_n, iters = cordas.cordas(eqn, a, b, prec)
        case 3:
            x0 = (a + b) / 2 # chute inicial razoável
            sqrt_n, iters = newton.newton(eqn, lambda x: 2 * x, x0, prec)
        case 4:
            res, n = iter_linear.iteracaoLinear(eqIntL,  FeqIntL, 1.5, 0.000000000000001)
            print(f"\nValor aproximado: {res} (iterações = {n})")
            exit(0)
        case 5:
            sqrt_n, iters = pegaso.pegaso(eqn, a, b, prec)
        case _:
            exit(0)

    ex = math.sqrt(n)
    print(f"\n=> Valor aproximado: {sqrt_n} (iterações: {iters})")
    print(f"Valor exato: {ex}")

if __name__ == "__main__":
    main()
