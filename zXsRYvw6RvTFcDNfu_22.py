
def fact(n):
    a = 2
    f = []
    while n > 1:
        if n % a == 0:
            f.append(a)
            n = n // a
        else:
            a += 1
    return [set(f),f]
​
def ruth_aaron(n):
    aa = 0
    bb = ''
    if sum(fact(n)[0]) == sum(fact(n-1)[0]):
        bb = 'Aaron'
        aa += 1
    elif sum(fact(n)[0]) == sum(fact(n+1)[0]):
        bb = 'Ruth'
        aa += 1
    if sum(fact(n)[1]) == sum(fact(n-1)[1]):
        bb = 'Aaron'
        aa += 2
    elif sum(fact(n)[1]) == sum(fact(n+1)[1]):
        bb = 'Ruth'
        aa += 2
​
    if aa == 0:
        return False
    return [bb,aa]

