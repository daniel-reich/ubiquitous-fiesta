
def sum_of_slices(lst):
    '''
    Returns a list containing the sum of slices of contiguous elements which
    satisfy the rules as per instructions.
    '''
    total, sums = lst[0], [] if lst[0] < 100 else [0]
​
    for i in range(1, len(lst)):
        if total + lst[i] <= 100:
            total += lst[i]
        else:
            sums.append(total)
            total = lst[i]
​
    return sums + [total]

