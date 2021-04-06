
def group(lst, size):
    """
    Slice a list into chunks of given size
    or equal size
    """
    from math import ceil
​
    if size < 1: return []
    
    bs = best_size(len(lst), size)
    chunks = ceil(len(lst)/bs)
​
    result = []
    for i in range(chunks):
        sub = []
        for j in range(bs):
            try: sub.append(lst[i+j*chunks])
            except: pass
        result.append(sub)
       
    return result
​
def best_size(lenght:int, max_size:int):
    """
    Find divisor of lenght that is equal
    or lesser than max_size
    """
    for size in  range(max_size, 1, -1):
        if lenght % size == 0:
            return  size
    return max_size

