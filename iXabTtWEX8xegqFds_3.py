
def alternate_sort(lst):
    sorted_alpha = sorted(i for i in lst if isinstance(i, str))
    sorted_num = sorted(i for i in lst if isinstance(i, int))
    return [x for i in zip(sorted_num, sorted_alpha) for x in i]

