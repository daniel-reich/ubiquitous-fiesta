
def waterjug(cap, goal):
    cap = tuple(cap + [cap[2]])
    goal = tuple(goal + [0])
    starting_state = (0, 0, cap[2], 0)
    steps = 0
    if starting_state[:3] == goal[:3]:
        return steps
    # depth first search
    prev_states = set()
    curr_states = set([starting_state])
    while curr_states:
        steps += 1
        next_states = set()
        for cs in curr_states:
            prev_states.add(cs)
            succ = possible_successors(cs, cap)
            for ns in succ:
                if ns not in prev_states:
                    if ns[:3] == goal[:3]:
                        return steps
                    next_states.add(ns)
        curr_states = next_states
    return "No solution."
​
​
def possible_successors(cs, cap):
    ret = []
    # a jug is poured into another until either is full or empty
    has_water = [i for i in range(len(cs)) if cs[i] > 0]
    under_cap = [i for i in range(len(cs)) if cs[i] < cap[i]]
    for h in has_water:
        for u in under_cap:
            if h != u:
                k = [0, 1, 2, 3]; k.remove(h); k.remove(u)
                unused = cap[u] - cs[u]
                if cs[h] > unused: # fill under_cap
                    poured = [(h, cs[h]-unused), (u, cap[u]), (k[0], cs[k[0]]), (k[1], cs[k[1]])]
                elif cs[h] <= unused: # empty has_water
                    if h == 3 and cs[h] != unused: # cannot partially fill empty jug
                        break
                    poured = [(h, 0), (u, cs[u]+cs[h]), (k[0], cs[k[0]]), (k[1], cs[k[1]])]
                poured = [p[1] for p in sorted(poured)]
                ret.append(tuple(poured))
    return list(set(ret))

