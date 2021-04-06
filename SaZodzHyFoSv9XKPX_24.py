
def domino_chain(dominos):
    for i in range(len(dominos)):
        if dominos[i] in '/ ':
            return dominos
        elif dominos[i] == '|':
            dominos = dominos[:i] + '/' + dominos[i+1:]
​
    return dominos

