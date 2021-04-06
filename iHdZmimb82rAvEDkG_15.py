
def parity(n):
    return 'even' if n//2 == n/2 else 'odd'
​
def bitwise_index(lst):
    lst = [(idx, i) for idx, i in enumerate(lst) if parity(i) == 'even']
    if not lst:
        return 'No even integer found!'
    idx_largest, n_largest = lst.pop(0)
    for idx, i in lst:
        if i > n_largest:
            idx_largest, n_largest = idx, i
    return {'@' + parity(idx_largest) + ' index ' + str(idx_largest): n_largest}

