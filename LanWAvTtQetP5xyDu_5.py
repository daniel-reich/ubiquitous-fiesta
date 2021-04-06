
from itertools import combinations
​
​
def coins_div(lst):
    len_lst, target = len(lst), sum(lst) / 3
    if len_lst < 3 or not target.is_integer() or max(lst) > target:
        return False
    elif len_lst == 3:
        return len(set(lst)) == 1
    lst.sort(reverse=True)
    target = int(target)
    first_comb = tuple()
    for size in range(1, len_lst - 1):
        for comb in combinations(lst, size):
            if sum(comb) == target:
                first_comb = comb
                break
        if first_comb:
            break
    if first_comb:
        for num in first_comb:
            lst.remove(num)
    else:
        return False
    second_comb = tuple()
    for size in range(1, len(lst)):
        for comb in combinations(lst, size):
            if sum(comb) == target:
                second_comb = comb
                break
        if second_comb:
            break
    if second_comb:
        return True
    return False

