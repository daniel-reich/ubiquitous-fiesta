
def zero_indices(lst, k):
    serie = [0, []]  # special case if array does not contain 1 | put index directly if K = 0
    for idx, elm in enumerate(lst):
        flips = k
        serie_len = 0
        flip_idx = []
​
        for sub_idx, sub_elm in enumerate(lst[idx:]):
            if sub_elm == 0 and flips <= 0: break
            if sub_elm == 0 and flips > 0:
                flips = flips - 1
                flip_idx.append(idx + sub_idx)
            serie_len += 1
​
        if serie_len > serie[0]: serie = [serie_len, flip_idx]
    return serie[1]

