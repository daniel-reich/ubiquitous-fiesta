
def count_missing_nums(lst):
    lst = sorted(lst)
    lst = [int(x) for x in lst if x.isdigit()]
    return (max(lst) - min(lst)) - (len(lst) - 1)

