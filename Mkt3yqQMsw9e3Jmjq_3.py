
def disjoint_cycle_form(perm):
    remaining, total = set(perm), set()
    while remaining:
        current_cycle = []
        ii = remaining.pop()
        while ii not in current_cycle:
            current_cycle.append(ii)
            ii = perm[ii]
        if len(current_cycle) > 1:
            total.add(tuple(current_cycle))
        remaining -= set(current_cycle)
    return total

