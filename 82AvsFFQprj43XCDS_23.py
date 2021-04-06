
def no_strangers(txt):
    txt = txt.lower()
    txt = ''.join([x for x in txt if x.isalpha() or x in " '"])
    txt = txt.split()
    d = {}
    friends = []
    acquaintances = []
    for x in txt:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
        if d[x] == 5:
            friends.append(x)
            acquaintances.remove(x)
        elif d[x] == 3:
            acquaintances.append(x)
    return [acquaintances, friends]

