
def multiply_by_11(n,k = 0,c = 0):
    if len(n) == 0:
        return str(int(k) + int(c))
    a = int(n[len(n)-1]) + int(k) + c 
    c = a // 10 if a > 9 else 0
    k = n[len(n)-1]
    n = n[:len(n)-1]
    return multiply_by_11(n,k,c) + str(a)[-1]

