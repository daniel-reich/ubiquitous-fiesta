
def min_length(lst, n):
    sublists = [
        len(lst[i_index:j_index])
        for i_index, _ in enumerate(lst)
        for j_index, _ in enumerate(lst, start=1)
        if sum(lst[i_index:j_index]) > n
    ]
    if sublists == []:
        return -1
    else:
        return min(sublists)

