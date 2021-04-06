
def primorial(n):
    mul = []
    mul1 = 1
    i = 0
    while True:
        if  not is_prime(i):
            i += 1
        elif is_prime(i):
            if len(mul) == n:
                break
            mul.append(i)
            i += 1
          
    for i in mul:
        mul1 *= i         
    return mul1
def is_prime(i):
    if i >= 2:
        for k in range(2,i):
            if not i % k:
                return False
    else:
        return False
    return True

