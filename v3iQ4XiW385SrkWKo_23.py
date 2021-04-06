
def final_result(lst):
    result = lst
    dropped = ['a']
    while dropped != [] and  len(result) > 1:
        result, dropped = find_dupes(result)
    return result
    
def find_dupes(lst):
    idx = 0
    dropped = []
    while idx < len(lst) - 1 : 
        if lst[idx] == lst [idx + 1]:
            while (idx + 1) < len(lst) and lst[idx] == lst [idx + 1]:            
                dropped.append(lst.pop(idx + 1)) 
            dropped.append(lst.pop(idx))
        idx = idx + 1
    return lst, dropped

