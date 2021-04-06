
def disjoint_cycle_form(perm):
    ordered = sorted(perm)
    permmap = dict(zip(ordered, perm))
    cycles = set()
    while ordered:
        a = ordered.pop(0)
        cycle = [a]
        while True:
            b = permmap[a]
            if b in cycle:
                break
            else:
                cycle.append(b)
                ordered.remove(b)
                a = b
        if len(cycle) > 1:
            m = min(cycle)
            while cycle[0] > m:
                cycle = cycle[1:] + (cycle[0],)
            cycles.add(tuple(cycle))
    return cycles

