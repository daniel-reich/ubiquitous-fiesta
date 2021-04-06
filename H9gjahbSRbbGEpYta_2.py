
def multiply(n1, n2):
    if n1 < 0 and n2 < 0:
        return sum(abs(n1) for _ in range(abs(n2)))
    elif n1 > 0 and n2 < 0:
        return sum(-n1 for _ in range(abs(n2)))
    return sum(n1 for _ in range(abs(n2)))

