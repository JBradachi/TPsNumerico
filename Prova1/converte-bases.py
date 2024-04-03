# REALIZAR CONVERSÕES DE BASES

def transformaParaBase10(base, numero):
    "Converte uma string de dígitos na base BASE e coverte para base 10"
    numeroTransformado = 0
    count = 0
    # Pega o tamanho da parte inteira do numero
    for a in range(len(numero)):
        count += 1
        if numero[a] == '.':
            count-=1
            break
    # Parte inteira do número
    for a in range(count):
        numeroTransformado += (base**(count-a-1))*int(numero[a])
    # Parte fracionária do número
    for a in range(1, len(numero)-count):
        numeroTransformado += (base**((-1)*(a)))*int(numero[count+a])
    return numeroTransformado

def transformaDeBase10ParaX(base, numero):
    "Converte um inteiro comum em uma string de dígitos na base BASE"
    dividendo = int(float(numero))
    valor = ""
    while dividendo != 0:
        valor = valor + str(dividendo%base)
        dividendo = int(dividendo/base) 
    
    valorDec = ""
    count = 0
    multi = float(numero)
    while multi > 0 and count<20:
        multi = multi - int(multi)
        multi = multi*base
        valorDec += str(int(multi))
        count += 1
        
    aux = ""
    for a in range(1, len(valor)+1):
        aux += valor[-a]
    aux = aux + "."
    return aux + valorDec

def main():
    print("\x1b[2J")
    print("="*50)
    print("PROGRAMA CONVERSOR DE BASES")
    print("="*50)
    num = str(input("Insira o numero a ser convertido (em float)\n>>> "))
    baseI = int(input("Insira a base do numero inserido\n>>> "))
    baseF = int(input("Insira a base para conversão\n>>> "))
    print("="*50)
    if(baseI == 10):
        print("O numero {} na base {} é igual a {} na base {}".format(num, baseI, transformaDeBase10ParaX(baseF, num), baseF))
    elif(baseF == 10):
        print("O numero {} na base {} é igual a {} na base {}".format(num, baseI, transformaParaBase10(baseI, num), baseF))
    else:
        print("O numero {} na base {} é igual a {} na base {}".format(num, baseI, transformaDeBase10ParaX(baseF, transformaParaBase10(baseI, num)), baseF))

if __name__ == "__main__":
    main()
