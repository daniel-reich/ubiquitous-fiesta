
def is_polydivisible(n):
    for i in range(1,len(str(n))+1):
        if int(str(n)[:i]) % i != 0:return False
    return True

