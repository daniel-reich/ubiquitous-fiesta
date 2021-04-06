
def josephus(people):
    p = list(range(1, people + 1))
    while len(p) > 1:
        p.append(p.pop(0))
        p = p[1:]
    return p[0]

