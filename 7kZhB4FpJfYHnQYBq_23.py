
def lcm_three(num):
    lista = []
    a, b, c = num[0], num[1], num[2]
    mini = min(a, b,c)
    maxi = a * b * c
    for n in range(mini, maxi + 1):
        if n % a == 0 and n % b == 0 and n % c == 0:
            lista.append(n)
    return lista[0]

