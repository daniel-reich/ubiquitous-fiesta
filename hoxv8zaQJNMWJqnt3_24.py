
def is_heteromecic(n):
    if n % 2 != 0:
        return False
    else:
        n = n // 2
        return cur(n)
def cur(n,i=0):
    if n - i < 0:
        return False
    elif n == i:
        return True 
    else:
        return cur(n-i,i+1)

