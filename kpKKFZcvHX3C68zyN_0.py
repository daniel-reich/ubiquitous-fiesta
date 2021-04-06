
def swap_cards(n1, n2):
    a, b, c, d = str(n1) + str(n2)
    if a <= b:
        a, c = c, a
    else:
        b, c = c, b
    return a + b > c + d

