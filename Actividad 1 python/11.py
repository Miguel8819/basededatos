M = [
 [2, 3],
 [6, 4],
]

N = [
 [2, 1],
 [6, 9],
]

s=[[M[i][j]+N[i][j] for j in range(len(M))] for i in range(len(N))] #Linea magica
print(M,"+", N, "=" , s)
