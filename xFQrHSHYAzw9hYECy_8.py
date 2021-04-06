
def lis(a):
    b=[]
    for i in range(len(a)):
        if a[i]!=a[i-1]:
            c=a[i]
        elif a[i]==a[i-1]:
            c+=a[i]
        if i==len(a)-1:
            b.append ( c )
        elif  a[i]!=a[i+1]:
                b.append(c)
    return b
​
​
def is_long_pressed(original, typed):
    a=lis(original)
    b=lis(typed)
    return len(a)==len(b) and all(len(a[i])<=len(b[i])for i in range(len(a)) )

