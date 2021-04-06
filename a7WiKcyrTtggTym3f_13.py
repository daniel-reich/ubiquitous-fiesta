
def lcm(a, b):
    num = 0
    for n in range(2, a*b+1):
        if n % a == 0 and n % b == 0:
            num = n
            break
    return num

