def pivotamento(A, B):
    n = len(A)
    for c in range(n-1):
        for l in range(c+1, n):
            if A[c][c] == 0:
                continue
            m = A[l][c] / A[c][c]
            A[l][c] = 0
            for i in range(c+1, n):
                A[l][i] = A[l][i] - m * A[c][i]
            B[l] = B[l] - m * B[c]

def gaus(A):
	n = len(A)
    
	X = [0 for i in range(n)]
	X[n-1] = B[n-1]/A[n-1][n-1]
	for i in range(n-2, -1, -1):
		soma = 0
		for j in range(i+1, n):
			soma = soma + A[i][j] * X[j]

		X[i] = (B[i] - soma)/A[i][i] 
  
	return X
  
  
def imprimirX(X):
    for i in range(len(X)):
    	print("X[",i,"] = ", X[i])
     
def imprimirSistema(A, B):
	n = len(A)
	print("Sistema após eliminação de Gauss:")
	for i in range(n):
		linha = ", ".join(f"{A[i][j]:8.4f}" for j in range(n))
		print(f"[{linha}]  | {B[i]:8.4f}")
         
A = [[2, 3,-1],
     [4, 4, -3],
     [2, -3, 1]]
B = [5, 3, -1]


print()
pivotamento(A, B)
X = gaus(A)
imprimirSistema(A, B)
print()
imprimirX(X)