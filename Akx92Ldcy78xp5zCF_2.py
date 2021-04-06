
def custom_sort(t, s):
    aux = ''
    for c1 in s:
        if c1 in t:
            aux += c1
            s = s.replace(c1, '')
    aux2 = ''
    for c2 in t:
        for c3 in aux:
            if c2 == c3:
                aux2 += c3
    return aux2 + ''.join(sorted(s))

