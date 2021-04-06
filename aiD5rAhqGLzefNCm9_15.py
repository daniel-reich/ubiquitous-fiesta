
def is_prime(num):
    sol, base, binary = 1, 2, str(bin(num - 1))[3:][::-1]
    for i in binary:
        if i == "1": sol = (sol*base) % num
        base = (base*base) % num
    return True if (sol*base) % num == 1 else False

