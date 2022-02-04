#1)a)
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[10,11,12],[13,14,15],[16,17,18]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
       for k in range(len(c)):
            c[i][j]+=a[j][k] * b[k][i]

for l in c:
    print(l)