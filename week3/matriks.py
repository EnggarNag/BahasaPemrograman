#Matriks dengan ukuran 2x2
matriksA = [
    [1,0], 
    [0,1]
    ]
matriksB = [
    [0,1], 
    [1,0]
    ]
matriksC = []  

print ("Matriks A :")
for x in range(0, len(matriksA)):
    for y in range(0, len(matriksA[0])):
        print (matriksA[x][y], end=' '),
    print ()
print ("Matriks B :")
for x in range(0, len(matriksB)):
    for y in range(0, len(matriksB[0])):
        print (matriksB[x][y], end=' '),
    print ()


print ("Jumlah Matriks:")
for i in range(0, len(matriksA)):
    jumlah = 0
    row =[]
    for j in range(0, len(matriksA[0])):
        jumlah = matriksA[i][j] + matriksB[i][j]
        row.append(jumlah)           
    print(row)
    matriksC.append(row)

