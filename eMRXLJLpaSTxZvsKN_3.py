
def is_ladder_safe(ldr):
    width = len(ldr[0])
    widths = [len(row) for row in ldr]
    if len(set(widths)) != 1 or width < 5 or len(ldr) < 3:
        return False
    gap = '#' + ' ' * (width - 2) + '#'
    rung = '#' * width
    if ldr[0] != gap or ldr[-1] != gap or ldr[-2] != rung:
        return False
    ldr.pop(0)
    ldr.pop()
    ldr.pop()
    if ldr[0] != rung:
        return False
    block = [rung]
    l = len(ldr)
    for i in range(1, l):
        if ldr[i] != gap:
            break
        block.append(gap)
    b = len(block)
    if l % b != 0 or len(block) > 3:
        return False
    return ldr == block * (l // b)

