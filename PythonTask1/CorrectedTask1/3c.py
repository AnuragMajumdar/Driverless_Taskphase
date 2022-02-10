a=['a','n','u','r','a','g']
b=''.join(a)
r=len(b)
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(a[j], end=" ")
    print()

for i in range(r):
    for j in range(i):
        print(" ",end="")
    for j in range(r-i):
        print(a[j], end=" ")
    print()

