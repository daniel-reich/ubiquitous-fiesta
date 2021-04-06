
def rank(lst):
    a = sorted(lst)
    vektor = []
    for i in range(0,len(a)):
        if a.count(a[i]) > 1:
            vektor.append(sum([y for y in range(0,len(a)) if a[y] == a[i]])/a.count(a[i]))
        else:
            vektor.append(float(i))
    result = []
    for i in lst:
        result.append(vektor[a.index(i)])
    return result

