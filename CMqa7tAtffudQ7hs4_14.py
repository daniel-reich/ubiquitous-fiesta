
def sorting_steps(items):
    '''
    Returns the item swaps needed to sort the elements in items as described
    above.
    '''
    from copy import deepcopy
    tester = deepcopy(items)  # so don't affect original
    steps = []
​
    # Select the steps necessary to perform a bubble sort
    for i in range(len(items) - 1):
        for j in range(len(items) - i - 1):
            if tester[j] > tester[j+1]:
                tester[j], tester[j+1] = tester[j+1], tester[j]
                steps.append((j,j+1)) # add the swap
​
    return steps

