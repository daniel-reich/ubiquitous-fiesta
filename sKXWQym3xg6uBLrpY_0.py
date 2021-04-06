
def iqr(lst):
    lst = sorted(lst)
    first_half = lst[:len(lst) // 2]
    second_half = lst[-(-len(lst) // 2):]
    first_half_median = (first_half[len(first_half) // 2] + first_half[~(len(first_half) // 2)]) / 2
    second_half_median = (second_half[len(second_half) // 2] + second_half[~(len(second_half) // 2)]) / 2
    return second_half_median - first_half_median

