
def chemical_reactions(carbon, hydrogen, oxygen):
    result = []
    d = {'c':carbon, 'h':hydrogen, 'o':oxygen}
    lst = [('h2', 'o1'), ('c1', 'o2'), ('c1', 'h4')]
    for (a, b) in lst:
        e1, n1 = a[0], int(a[1])
        e2, n2 = b[0], int(b[1])
        molecules = min(d[e1]//n1, d[e2]//n2)
        result.append(molecules)
        d[e1] -= molecules * n1
        d[e2] -= molecules * n2
    return result

