
def divide(numbers, size):
    '''
    Returns a list of lists where each sublist is a contiguous subset of numbers
    such the sum of its elements does not exceed size.
    '''
    groups = []
    current = []
​
    for num in numbers:
        if sum(current) + num <= size:
            current.append(num)
        else:
            groups.append(current)
            current = [num]  # start a new subgroup
​
    if current:
        groups.append(current)  # add last subgroup if it contains numbers
​
    return groups

