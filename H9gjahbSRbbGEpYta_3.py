
def multiply(n1, n2):
    positive = True
    if n1 < 0:
        n1 = -n1
        positive = not positive
    if n2 < 0:
        n2 = -n2
        positive = not positive
    n1, n2 = (n1, n2) if n1 >= n2 else (n2, n1)
    res = sum(n1 for _ in range(n2))
    return res if positive else -res

