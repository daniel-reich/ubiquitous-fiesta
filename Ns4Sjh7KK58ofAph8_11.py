
def is_triplet(n1, n2, n3):
    a = list()
    a.append(n1)
    a.append(n2)
    a.append(n3)
    a.sort()
    if a[0]**2+a[1]**2==a[2]**2:
        return True
    return False

