
def dice_game(lst: list) -> str:
    p = ['p1', 'p2', 'p3', 'p4']
    i = 0
    while True:
        temp = [[sum(j), j[0]] for j in lst[i:i+len(p)]]
        i += len(p)
        l = list(zip(*temp))
        x = min(l[0])
        if l[0].count(x) == 1:
            y = l[0].index(x)
            p.pop(y)
        elif l[0].count(x) >= 1:
            z = min(l[1])
            if l[1].count(z) == 1:
                r = l[1].index(z)
                p.pop(r)
        if len(p) == 1:
            return p[0]

