
def domino_chain(dominos):
    i = 0
    for x in dominos:
        if x != '|':
            break
        i += 1
    return i * '/' + dominos[i:]

