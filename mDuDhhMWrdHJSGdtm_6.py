
def is_prime(num):
    if num == 2: return True
    sol, base, binary = 1, 2, str(bin(num - 1))[3:][::-1]
    for i in binary:
        if i == "1":
            sol = (sol*base) % num
        base = (base*base) % num
    return (sol*base) % num == 1
​
def is_exactly_three(n):
    return is_prime(int(n**0.5)) if n**0.5 == int(n**0.5) else False

