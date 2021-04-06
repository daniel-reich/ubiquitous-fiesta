
def loves_me(n):
    a=''
    a1='Loves me, '
    a2='Loves me not, '
    for x in range(n):
        if x%2==0:
            if x+1==n:
                a+=a1[:-2].upper()
            else:
                a+=a1
        else:
            if x+1==n:
                a+=a2[:-2].upper()
            else:
                a+=a2
    return a

