
def cycle_length(lst, n, sorted_lst=[]) -> int:
    if not sorted_lst:
        sorted_lst = sorted(lst)
    i = lst.index(n)
    si = sorted_lst.index(n)
    if i == si:
        return 0
    else:
        lst[i], lst[si] = lst[si], lst[i]
        return 1 + cycle_length(lst, lst[i], sorted_lst)

