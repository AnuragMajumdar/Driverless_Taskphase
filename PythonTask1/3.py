a=['m','a','l','a','y','a','l','a','m']
r=''.join(a)
def reverse(r):
    if len(r)==1:
        return r
    else:
        return reverse(r[1:]) + r[0]
s=(reverse(r))
print(s)
def check_palindrome(s):
    if s==r:
        return True
    else:
        return False
print(check_palindrome(s))

for i in a:
    print(hex(ord(i)))





