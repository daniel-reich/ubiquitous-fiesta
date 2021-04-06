
def find_fulcrum(lst):
    '''
    Returns the 1st number in lst whose values to its left sum to its values
    to its right, or -1 if there is no such number
    '''
    for i in range(1, len(lst)-1):
        if sum(lst[0:i]) == sum(lst[i+1:]):
            return lst[i]
    return -1

