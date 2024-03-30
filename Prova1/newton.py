#!/usr/bin/env python3
# newton.py: estima as raízes das funções pelo método de newton


def metodoNewton(fn, dfn, x0, erro):
    if dfn==0:
        print("Erro, não é possível usar o método")
        return 0
    MAX_ITERS = 1000
    n = 0
    xn = 0
    x =0
    while n < MAX_ITERS and erro < abs(x0-x):
        print("n=", n, "xn=", x0, "fn=", (fn(x0)), "erro=", abs(x0-x))
        xn = x0 - (fn(x0) / dfn(x0))
        x = x0
        x0 = xn
        n+=1
    return print("n=", n, "xn=", x0, "fn=", (fn(x0)), "erro=", abs(x0-x))

def fx(x):
        return x*x - 8
    
def dfx(x):
    return 2*x
        
metodoNewton(fx, dfx, 3, 0.001)
