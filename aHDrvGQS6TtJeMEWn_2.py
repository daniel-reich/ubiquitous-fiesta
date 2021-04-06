
def max_sum_pair(lst):
    len_lst = len(lst)
    max_sums = min(lst)
    for b1 in range(len_lst):
        for e1 in range(b1, len_lst + 1):
            for b2 in range(e1, len_lst):
                for e2 in range(b2, len_lst + 1):
                    s = sum(lst[b1: e1]) + sum(lst[b2:e2])
                    if s > max_sums:
                        max_sums = s
    return max_sums

