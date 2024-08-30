# Integral dupla pela primeira regra de Simpson
import math

def simpson(function, a, b, n):
    if n % 2 != 0 or n<1:
        print('ERRO! N deve ser par e maior que 0')
        return 
   
    h = (b - a) / n
    soma_impar, soma_par = 0, 0
    for k in range(1, n, 2):
        soma_impar += function(a + k * h)
    for k in range(2, n, 2):
        soma_par += function(a + k * h)
        
    return (h / 3) * (function(a) + 4 * soma_impar + 2 * soma_par + function(b))




# Função para integração dupla usando a regra de Simpson
def calc_integral_dupla(f, a, b, c, d, n):
    if n % 2 != 0 or n < 1:
        print('ERRO! N deve ser par e maior que 0')
        return 
    
    # Intervalo de integração para y
    hy = (d - c) / n
    soma_impar, soma_par = 0, 0
    
    # Função auxiliar para integração em x para cada y fixo
    def integral_x_fixo_y(y):
        return simpson(lambda x: f(x, y), a, b, n)
    
    # Aplicando Simpson em y
    for j in range(1, n, 2):
        soma_impar += integral_x_fixo_y(c + j * hy)
    for j in range(2, n, 2):
        soma_par += integral_x_fixo_y(c + j * hy)
    
    # Resultado final aplicando a regra de Simpson para y
    integral = (hy / 3) * (integral_x_fixo_y(c) + 4 * soma_impar + 2 * soma_par + integral_x_fixo_y(d))
    return integral




# Função a ser integrada
def function_2d(x, y):
    # Exemplo de função: exp(-x^2 - y^2)
    return math.exp(-x**2 - y**2)

# Limites de integração de x
a, b = 0, 1
# Limites de integração de y
d, c = 0, 1

# N = Numero de subintervalos 
# N/2 = Numero de parábolas
# N + 1 = Numero de pontos
n = 500


integral = calc_integral_dupla(function_2d, a, b, d, c,  n)

print(f'\nResultado Integral: {integral}')