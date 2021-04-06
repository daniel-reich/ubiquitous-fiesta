
def num_type(n):
    suma = 0
    s1 = 0
    for a in range(1, n, 1):
        if n %a == 0:
            suma +=a
​
    if suma == n:
        return 'Perfect'
    else:
        for i in range(1 , suma, 1):
            if suma %i == 0:
                s1 += i
        if s1 == n :
            return 'Amicable'
        else:
            return 'Neither'

