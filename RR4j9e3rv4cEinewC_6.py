
def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def lcm(a, b):
    return (a * b) // gcd(a, b)
​
def hats(lst):
    n, prod = lst
    l = lcm(lcm(lcm(lcm(prod[0], prod[1]), prod[2]), prod[3]), prod[4])
    time = 0
    all_even = sum([l // prod[i] for i in range(5)])
    while n >= all_even:
        n -= all_even
        time += l
    while n > 0:
        time += 1
        for i in range(5):
            r = time / prod[i]
            if time >= prod[i] and abs(r - int(r)) < 1e-4:
                n -= 1
    if n == 0:
        return "1 minute" if time == 1 else str(time) + " minutes"

