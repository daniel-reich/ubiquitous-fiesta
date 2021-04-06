
def factorial(n):
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    else:
        return n * factorial(n - 1)
​
​
def nPr(n, r):
    result = 1
    for num in range(n - r + 1, n + 1):
        result *= num
    return result
​
def nCr(n, r):
    if r <= n //2:
        return nPr(n, r) // factorial(r)
    else:
        result = 1
        for num in range(r+1, n+1):
            result *= num
        return result // factorial(n-r)

