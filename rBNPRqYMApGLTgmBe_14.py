
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n - 1) * n
​
​
def combinations(k, n):
    part1 = factorial(n)
    part2 = factorial(k)
    part3 = factorial(n - k)
    return int(part1 / (part2 * part3))

