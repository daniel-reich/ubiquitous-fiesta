
def no_strangers(txt):
    t = txt.translate(str.maketrans('', '', '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')).lower().split()
    frequency = {}
    a = {3: [], 5: []}
    for x in t:
        frequency[x] = frequency.get(x, 0) + 1
        if frequency[x] == 3:
            a[3].append(x)
        elif frequency[x] == 5:
            a[3].remove(x)
            a[5].append(x)
    return [x for x in a.values()]

