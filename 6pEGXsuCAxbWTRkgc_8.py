
def loves_me(n):
    s= []
    if n==1:
        return 'LOVES ME'
    for i in range(n-1):
        if i%2==0:
            s.append('Loves me')
        else:
            s.append('Loves me not')
    a=', '.join(s)
    if s[-1]=='Loves me':
        return a+', '+'LOVES ME NOT'
    else:
        return a+', '+'LOVES ME'

