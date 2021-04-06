
def two_product(lst, target):
    '''
    Returns the first 2 numbers in lst whose product = target, or None if
    there isn't one.
    '''
    for i, num in enumerate(lst):
        if num and not target %num:
            other = target // num
            if other in lst[i+1:]:
                return [min(num,other), max(num,other)]

