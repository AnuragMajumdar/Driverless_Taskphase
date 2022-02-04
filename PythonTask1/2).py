a=(1,1,2,2,3,3,4,4,5,5,6,6)
b=set(a)
c=list(b)
print(b)
def sum(c,d ):
    if len(c):
        return sum(c[1:], d+c[0])
    else:
        return d
print(sum(c,0))