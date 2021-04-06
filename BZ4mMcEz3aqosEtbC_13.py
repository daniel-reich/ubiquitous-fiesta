
def mean(n):
    s = 0
    card = 0
    while n != 0:
        s += n % 10
        n = n // 10
        card += 1
        
    return s//card

