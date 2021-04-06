
def is_exactly_three(n):
    a = 0
    if n == 1:
        return False
​
    i = 2
    while i*i <= n:
        if not n % i or not n % 10:
            if a == 2:
                return a == 1
            a += 1
        i += 1
    return a == 1

