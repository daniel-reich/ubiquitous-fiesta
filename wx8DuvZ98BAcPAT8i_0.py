
def move_discs(start, end):
    s_left = start[:3].rstrip('0')
    s_middle = start[3:5].rstrip('0')
    s_right = start[5:].rstrip('0')
    e_left = end[:3].rstrip('0')
    e_middle = end[3:5].rstrip('0')
    e_right = end[5:].rstrip('0')
    s_state = (s_left, s_middle, s_right)
    e_state = (e_left, e_middle, e_right)
    visited = {s_state}
    states = [[s_state, []]]
    n_moves = 0
    while states:
        n_moves += 1
        new_states = []
        for st in states:
            lt, md, rt = st[0]
            moves = st[1]
            len_lt, len_md, len_rt = len(lt), len(md), len(rt)
            if lt != e_state[0][:len_lt] and len_lt:
                if len(md) < 2:
                    new_state = (lt[:-1], md + lt[-1], rt)
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->M'.format(lt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
                if len(rt) < 3:
                    new_state = (lt[:-1], md, rt + lt[-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->R'.format(lt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
​
            if md != e_state[1][:len_md] and len_md:
                if len(lt) < 3:
                    new_state = (lt + md[-1], md[:-1], rt)
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->L'.format(md[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
                if len(rt) < 3:
                    new_state = (lt, md[:-1], rt + md[-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->R'.format(md[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
​
            if rt != e_state[2][:len_rt] and len_rt:
                if len(lt) < 3:
                    new_state = (lt + rt[-1], md, rt[:-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->L'.format(rt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
                if len(md) < 2:
                    new_state = (lt, md + rt[-1], rt[:-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->M'.format(rt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
        states = new_states
    """We should never get to this point"""
    return 'Not possible to reach the end state from the start state'

