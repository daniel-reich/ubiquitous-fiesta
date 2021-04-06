
def priority_sort(lst, s):
    return sorted(lst, key=lambda x: (-(x in s), x))

