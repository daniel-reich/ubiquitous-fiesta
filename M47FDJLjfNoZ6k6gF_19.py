
def cup_swapping(swaps):
    pos = 'B'
    for swap in swaps:
        if swap == 'AB' or swap == 'BA':
            if pos == 'C': 
                continue
            if pos == 'B':
                pos = 'A'
            else:
                pos = 'B'
        elif swap == 'BC' or swap == 'CB':
            if pos == 'A':
                continue
            if pos == 'B':
                pos = 'C'
            else:
                pos = 'B'
        else:
            if pos == 'B':
                continue
            if pos == 'A':
                pos = 'C'
            else:
                pos = 'A'
    return pos

