
def disjoint_cycle_form(perm):
    map_ = {a: b for a, b in zip(sorted(perm), perm) if a != b}
    disjoint = set()
    
    while map_:
        i = min(map_)
        group = []
        while i in map_:
            j = map_[i]
            group.append(i)
            del map_[i]
            i = j
        disjoint.add(tuple(group))
        
    return disjoint

