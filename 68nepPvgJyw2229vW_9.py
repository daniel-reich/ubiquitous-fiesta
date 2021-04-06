
def pairwise_swap(lst):
    len_lst = len(lst)
    if len_lst < 2:
        return lst
    for i in range(0, len_lst - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    if len_lst % 2:
        idx = max_val = 0
        for i, e in enumerate(lst):
            ascii_val = 0
            for c in str(e):
                ascii_val += ord(c)
            if ascii_val > max_val:
                idx = i
                max_val = ascii_val
        lst[idx], lst[len_lst - 1] = lst[len_lst - 1], lst[idx]
    return lst

