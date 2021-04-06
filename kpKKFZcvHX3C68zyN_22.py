
def swap_cards(n1, n2):
    n1, n2 = str(n1), str(n2)
    n1,n2 = (n2[0]+n1[1], n1[0]+n2[1]) if n1[0]<=n1[1] else (n1[0]+n2[0], n1[1]+n2[1])
    return n1>n2

