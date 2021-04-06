
def domino_chain(dominos):
    if len(dominos) == 0 or dominos[0] != '|':
        return dominos
    dominos = list(dominos)
    idx = 0
    while idx < len(dominos) and dominos[idx] == '|':
        dominos[idx] = '/'
        idx += 1
    return ''.join(dominos)

