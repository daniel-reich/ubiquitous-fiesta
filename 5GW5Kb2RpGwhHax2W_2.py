
def spiral_transposition(lst):
    return list(lst[0]) + spiral_transposition(list(zip(*lst[1:]))[::-1]) if lst else []

