
def sum_first_n_nums(lst, n):
    if n > len(lst):
        n = len(lst)
    return sum(lst[i] for i in range(n))

