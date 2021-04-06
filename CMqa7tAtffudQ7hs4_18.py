
from copy import copy
def sorting_steps(lst):
    swaps = []
    if len(lst) == 0 or len(lst) == 1 :
        return []
    print (lst)
    correct = {} 
    for u in set(lst):
        v = [pair[1] for pair in zip(sorted(lst),range(len(lst))) if pair[0] == u]
        correct[u] = v
    print (correct)
    while lst != sorted(lst):
        num = [k for k,v in correct.items() if len(v)>0][0]
        num_pos = lst.index(num)
        num_corr = correct[num].pop()
        print(num, num_pos, num_corr)
        while num_corr != num_pos and lst[num_corr] != num:
            swaps.append([num_corr, num_pos])
            lst[num_corr], lst[num_pos], num = num, lst[num_corr], lst[num_corr]
            print (lst)
            num_pos = lst.index(num)
            if len(correct[num]) == 0:
                break
            num_corr = correct[num].pop()
            print(num, num_pos, num_corr)
    return swaps

