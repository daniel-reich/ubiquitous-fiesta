
def sum_list(lst):
    total = 0  
    for i in lst:
        if isinstance(i, list): 
            total += sum_list(i)
        else:
            total += i
    return total

