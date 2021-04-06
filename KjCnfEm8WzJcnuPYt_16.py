
from itertools import combinations
​
​
def longest_contiguous(lst):
    max_len_ones, ones_begin, contiguous = 0, 0, False
    for i in range(len(lst)):
        if lst[i] == 1:
            if not contiguous:
                contiguous = True
                ones_begin = i
            elif i == (len(lst) - 1) and contiguous:
                len_ones = i - ones_begin + 1
                if len_ones > max_len_ones:
                    max_len_ones = len_ones
        elif lst[i] == 0:
            if contiguous:
                contiguous = False
                len_ones = i - ones_begin
                if len_ones > max_len_ones:
                    max_len_ones = len_ones
    return max_len_ones
​
​
def zero_indices(lst, k):
    zero_pos = [i for i, val in enumerate(lst) if not val]
    flipped = []
    for tpl in combinations(zero_pos, k):
        tmp_lst = lst[:]
        for j in tpl:
            tmp_lst[j] = 1
        flipped.append((-longest_contiguous(tmp_lst), tpl))
    flipped.sort()
    return list(flipped[0][1])

