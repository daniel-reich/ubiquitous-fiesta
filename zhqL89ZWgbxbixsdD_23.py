
def recursion(n, k):
    if k <= 1:
        return n == 1
    if n % k != 0:
        return False
    n //= k
    if n <= 1:
        return True
    return recursion(n, k - 1)
​
def is_exact(n):
    k = 2
    while True:
        a = recursion(n, k)
        if a:
            return [n, k]
        if k > 50:
            return "Not exact!"
        k += 1

