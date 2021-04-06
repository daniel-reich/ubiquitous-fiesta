
def priority_sort(lst, s):
    return [el[0] for el in sorted([[k, k in s] for k in lst], key=lambda x: (-x[1], x[0]))]

