
def pairwise_swap(lst):
    if len(lst) < 2:
        return lst
    
    res = []
    if not len(lst)%2:
        for i in range(0, len(lst), 2):
            res += [lst[i+1], lst[i]]
        return res
    else:
        last = lst.pop()
        for i in range(0, len(lst), 2):
            res += [lst[i+1], lst[i]]
        res.append(last)   
        ascii_max = max(res, key= lambda x: sum(map(ord, str(x))))
    swap_idx = res.index(ascii_max)
    res[-1], res[swap_idx] = res[swap_idx], res[-1]
    
    return res

