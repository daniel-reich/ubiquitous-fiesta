
def vigenere(a, b):
    l = [chr(i) for i in range(65, 91)]
    z = ""
​
    def key(p, b, k):
        j = 0
        for i in p:
            k += b[j % len(b)].upper()
            j += 1
        return k
    if a[1].islower():
        p = "".join([i.upper() for i in a if i.isalpha()])
        k = key(p, b, "")
        for i in range(len(p)):
            x = l.index(p[i])
            y = l.index(k[i])
            z += l[(x + y) % 26]
    else:
        k = key(a, b, "")
        for i in range(len(k)):
            x = l.index(k[i])
            q = 0
            while l[(x + q) % 26] != a[i]:
                q += 1
            z += l[q]
    return z

