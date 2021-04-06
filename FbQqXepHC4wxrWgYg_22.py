
def prime_divisors(num):
    b = [i for i in range(2, num+1) if num%i ==0]
    p = []
    for i in b:
        a = [j for j in range(2, i+1) if i%j ==0]
        if len(a) == 1:
            p.extend(a)
    return p

