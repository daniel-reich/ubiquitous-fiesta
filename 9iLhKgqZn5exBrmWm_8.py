
def ascending(seq):
    '''
    Returns True if seq has a sequence of at least 2 ascending & consecutive
    numbers.
    '''
    size = len(seq)
​
    for j in range(1, size//2 + 1):
        if size % j == 0:
            if all([int(seq[i:i+j]) == int(seq[i-j:i]) + 1 for i in range(j, size, j)]):
                return True
​
    return False

