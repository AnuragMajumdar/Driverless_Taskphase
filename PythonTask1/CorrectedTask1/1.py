p=int(input("Enter the no. of rows in the matrix1:"))
q=int(input("Enter the no. of columns in the matrix2:"))
n=int(input("Enter the no. of columns in the matrix1 or no. of rows in matrix 2:"))

print("Enter the elements of matrix 1:")
matrix1=[[int(input()) for a in range(n)] for b in range(p)]
print("matrix1:")
for a in range(p):
    for b in range(n):
        print(format(matrix1[a][b],"<4"),end="")
    print()

print("Enter the elements for matrix 2:")
matrix2=[[int(input()) for a in range(q)] for b in range(n)]
print("matrix2:")
for a in range(n):
    for b in range(q):
        print(format(matrix2[a][b],"<4"),end="")
    print()


result1=[[0 for a in range(q)]for b in range(p)]

for a in range(p):
    for b in range(q):
        for c in range(n):
            result1[a][b] = result1[a][b] + matrix1[a][c] * matrix2[c][b]

print("result=")
for a in range(p):
    for b in range(q):
        print(format(result1[a][b],"<5"),end="")

#Transpose of matrix
result=[[0 for a in range(p)] for b in range(q)]

for a in range(p):
    for b in range(q):
        result[a][b] = matrix1[b][a]

print("\ntranspose result of matrix 1: ")
for a in range(q):
    for b in range(p):
       print(format(result[a][b],"<4"),end="")

for a in range(p):
    for b in range(q):
        result[a][b] = matrix2[b][a]

print("\ntranspose result of matrix 2: ")
for a in range(q):
    for b in range(p):
       print(format(result[a][b],"<4"),end="")

#Multiplication of transpose of matrix
result2=[[0 for a in range(q)]for b in range(p)]

for a in range(p):
    for b in range(q):
        for c in range(n):
            result2[a][b] = result2[a][b] + matrix1[a][c] * matrix2[c][b]

print("\nresult of transpose of matrix=")
for a in range(p):
    for b in range(q):
        print(format(result2[a][b],"<5"),end="")




