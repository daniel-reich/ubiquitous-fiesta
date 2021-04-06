
def swap_two(txt):
    if len(txt) < 4: return txt
    return txt[2:4] + txt[:2] + ''.join(swap_two(txt[4:]))

