
def sum_first_n_nums(lst, n):
    i = 0
    sum = 0
    if n >= len(lst):
        while i < len(lst):
            sum = sum + lst[i]
            i = i + 1
        return sum
    else:
        while i < n:
            sum = sum + lst[i]
            i = i + 1
        return sum

