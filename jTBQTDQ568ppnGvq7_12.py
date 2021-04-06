
def digit_sort(lst):
    return sum([sorted([i for i in lst if len(str(i))==j]) for j in set([len(str(i)) for i in lst])][::-1], [])

