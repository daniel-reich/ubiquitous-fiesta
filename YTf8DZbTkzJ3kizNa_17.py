
def is_prime(m):
    lista = list(range(2, m))
    for i in lista:
​
        if m % i==0:
​
            return False
    return True
​
​
def moran(n):
    con=list((str(n)))
    ana=sum((int(i)) for i in con)
    ar=int(n/ana)
    if is_prime(ar)==True:
        return "M"
    elif n%ana==0:
        return "H"
​
    else:
        return "Neither"

