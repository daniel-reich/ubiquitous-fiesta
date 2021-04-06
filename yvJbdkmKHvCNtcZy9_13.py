
def is_disarium(n):
    a = [int(i) for i in list(str(n))]
​
    b = [i + 1 for i in range(len(a))]
​
    return sum([x ** y for x, y in zip(a, b)]) == n

