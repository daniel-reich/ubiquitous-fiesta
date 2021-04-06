
def is_triplet(n1, n2, n3):
    liczby=[n1,n2,n3]
    liczby.sort()
    print(liczby)
    return liczby[0]**2+liczby[1]**2==liczby[2]**2

