
def is_triplet(n1, n2, n3):
    a =[n1,n2,n3]
    a.sort()
    return a[0]**2 + a[1]**2 == a[2]**2

