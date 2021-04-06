
def sum_first_n_nums(lst, n):
    sum = 0
    
    if n > len(lst):
        n = len(lst)
    
    for i in range(n):
        sum += lst[i]
    
    return sum

