
def func(n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)
    return s-(len(n)**2)

