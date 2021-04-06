
def is_early_bird(length, n):
    '''
    Returns a list of the indices of the positions where n appears in the
    sequence of integers from 0 to length as per instructions, plus 'Early Bird'
    if the number appears before its natural position.
    '''
    n_str = str(n)
    size = len(n_str)
    seq = ''.join(map(str, list(range(length + 1))))
    indices = []
    idx = seq.find(n_str)
​
    while idx != -1:
        indices.append([idx + i for i in range(size)])
        idx = seq.find(n_str, idx+1)
​
    if len(indices) > 1:
        indices.append('Early Bird!')
​
    return indices

