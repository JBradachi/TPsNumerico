"""
    Aplica o método da iteração linear para estimar a raiz da função
    NOTA: fn(a) * fn(b) < 0 é assumido como condição inicial!
    NOTA: F'(x0) < 1 é assumido como condição inicial!
"""
import math

def interacaoLinear(fx, Fx, x0 , prec):
    n = 0
    MAX_ITERS = 1000
    while n < MAX_ITERS:
        """O método da iteração linear permite calcular o valor da raiz 
        inserindo a aproximação anterior em ou função (F(x)) obtida manipulando 
        a função inicial f(x) = 0. A função deve atendar a condição de que
        sua segunda derivada de ser < 1""" 


        x = Fx(x0)
        erro = abs(x - x0) 

        print("n=", n, "xn=", x0, "fn=", (fx(x0)), "erro=", erro, "Fn = ",Fx(x0))

        if erro < prec:
            return x, erro  # precisão desejada foi alcançada
        # Do contrário, o processo continua com novos valores para x0 e x1
        x0 = x
        n += 1
        
    return x, erro  # limite de iterações atingido, retorna melhor aproximação

def main():
    # Exemplo de aplicação x^3-x-1
    def f(x):
        return (math.pow(x, 3)) - x - 1
    # F(x) Obtida isolando x^3  ((x+1)^(1/3))
    def F(x):
      return math.pow((x+1), 1/3)
    res, err = interacaoLinear(f,  F, 1.5, 0.000000000000001)
    print(f"\nAproximação: {res} (erro = {err})")


if __name__ == "__main__":
    main()

    