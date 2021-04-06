
def classify_rug(m):
    a = len(m)
    v1 = []
    v2 = []
    if a%2 == 0:
        v1 = m[:a//2]
        v2 = m[a//2:]
    else:
        v1 = m[:a//2+1]
        v2 = m[a//2:]
    b = len(m[0])
    h1 = []
    h2 = []
    if b%2 == 0:
        for i in m:
            h1.append(i[:b//2])
            h2.append(i[b//2:])
    elif b %2 != 0:
        for i in m:
            h1.append(i[:b//2 +1])
            h2.append(i[b//2:])
    if v1 == v2[::-1] and h1[-1] != h2[-1][::-1]:
        return "horizontally symmetric"
    elif h1[-1] == h2[-1][::-1] and v1 != v2[::-1]:
        return "vertically symmetric"
    elif h1[-1] == h2[-1][::-1] and v1 == v2[::-1]:
        return "perfect"
    else:
        return "imperfect"

