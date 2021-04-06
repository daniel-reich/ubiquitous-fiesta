
def how_bad(n):
    num = bin(n)
    l = list(num[2:]).count('1')
    res =[]
    if l%2==0:res.append('Evil')
    else:res.append('Odious')
    if prime(l)==True:res.append('Pernicious')
    return res
def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:return False
        return True
    return False

