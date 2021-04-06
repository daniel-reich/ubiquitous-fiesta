
def multiply(n1, n2):
    total = 0
    x = 1 if n2>0 else -1
    while n2 != 0:
        total += n1
        n2 -= x
    return total if x==1 else total-total-total

