
def is_ladder_safe(ldr):
    width = max(len(i) for i in ldr)
    rungs, other = '#' * width, '#' + ' '*(width-2) + '#'
    correct_ends = ldr[:2] == [other, rungs] and ldr[-2:] == [rungs, other]
    
    if not correct_ends or width < 5:
        return False
    
    rung_pos = [idx for idx, i in enumerate(ldr) if i == rungs]
    gaps = [b - a for a, b in zip(rung_pos, rung_pos[1:])]
    return gaps[0] <= 3 and len(set(gaps)) == 1

