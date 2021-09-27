matriz1=[[1,2,3],
        [4,5,6],
        [7,8,9]]

matriz2=[[1,2,3],
        [4,5,6],
        [7,8,9]]
matriz3=[[0,0,0],
        [0,0,0],
        [0,0,0]]
filas=3
columnas=3
for i in range(filas):   
    for j in range (columnas):
        matriz3[i][j]=matriz1[i][j]*matriz2[i][j]
        
for r in matriz3:
    print (r)