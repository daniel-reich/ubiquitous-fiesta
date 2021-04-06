
def full_cycle(lst):
​
    dict_1, dict_2 = {}, {}
    curr_val, next_ind = lst[0], lst[0]
​
    if max(lst)> len(lst) - 1:
            return False
​
    for i in range(max(lst) + 1):
        dict_1[str(i)] = 1
        dict_2[str(i)] = 0
        if lst.count(lst[i]) > 1:
            return False
        
    while next_ind != 0:
        if max(dict_2.values()) > 1:
            return False
        dict_2[str(curr_val)] += 1
        next_ind = curr_val
        curr_val = lst[next_ind]
​
    return dict_1 == dict_2

