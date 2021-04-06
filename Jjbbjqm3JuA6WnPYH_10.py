
def numbertobit(n):
    s=''
    while n!=0:
        s+=str(n%2)
        n//=2
    return s[::-1]
​
def bittonumber(s):
    n=0
    a=1
    for i in s[::-1]:
        n+=int(i)*a
        a*=2
    return n
​
def bit_rotate(n, m, d):
    n1=numbertobit(n)
    if d:
        n1=n1[len(n1)-m:]+n1[:len(n1)-m]
    else :
        n1=n1[m:]+n1[:m]
    return bittonumber(n1)

