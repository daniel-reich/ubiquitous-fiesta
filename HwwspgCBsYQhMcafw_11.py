
def sd(n):
    return n if n < 10 else sd(sum([int(d) for d in str(n)]))
​
def super_digit(n, k):
    n = str(n) * k
    return sd(int(n))

