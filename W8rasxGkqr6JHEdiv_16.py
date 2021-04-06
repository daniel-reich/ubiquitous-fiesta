
def countdown(operands, target):
    '''
    Returns a string containing an expression so that each number in nums
    is combined to reach target
    '''
    from itertools import permutations
    
    ops = (' +',' -',' *','//')
    selections = [str(num)+op for op in ops for num in operands]
    
    for combo in permutations(selections, len(operands)):
        nums = [term[:-2] for term in combo]
        if any(nums.count(term) > 1 for term in nums):
            continue
        expr = ''.join(term for term in combo)[:-2]
        if eval(expr) == target:
            return expr.replace(' ','')
​
    return 'Failed to find it!!!'

