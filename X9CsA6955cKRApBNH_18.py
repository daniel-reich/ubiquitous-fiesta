
def longest_run(numbers):
    '''
    Returns the length of the longest consecutive run in numbers, where a run is
    a sequence of integers differing either by 1 (ascending) or -1 (descending).
    '''
    from operator import add, sub
    
    max_count = 1
    size = len(numbers)
​
    for op in(add, sub):
        i = j = 0
        count = 1
        
        while i < size-1:
            while j < size-1 and op(numbers[j], 1) == numbers[j+1]:
                count += 1
                j+= 1
            if count > max_count:
                max_count = count
            i, j = j, j+1
            count = 1
    
    return max_count

