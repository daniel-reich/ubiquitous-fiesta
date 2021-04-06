
def domino_chain(dominos):
    '''
    Returns the dominos after any which can fall have done so
    '''
    i, size = 0, len(dominos)
    new_state = ''
​
    while i < size and dominos[i] == '|':
        new_state += '/'
        i += 1
​
    return new_state + dominos[i:]

