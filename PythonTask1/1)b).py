#1)b)
a=[[1,2,3],[4,5,6]]
b=[[0,0],[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        b[j][i] = a[i][j]

for k in b:
    print(k)