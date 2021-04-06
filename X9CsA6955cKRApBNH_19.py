
def longest_run(lst):
    max_run = 1
    i = -1
    cur_run = 1
    if len(lst) == 0:
        return 0
    
    while i < len(lst)-1:
        if lst[i] + 1 == lst[i + 1]:
            cur_run += 1
            i += 1
            if cur_run > max_run:
                max_run = cur_run
        else:
            cur_run = 1
            i += 1
​
    i = -1
    cur_run = 1
    while i < len(lst)-1:
        if lst[i] -1 == lst[i + 1]:
            cur_run += 1
            i += 1
            if cur_run > max_run:
                max_run = cur_run
        else:
            cur_run = 1
            i += 1        
    
    return max_run

