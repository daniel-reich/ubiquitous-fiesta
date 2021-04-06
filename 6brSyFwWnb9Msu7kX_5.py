
def pos_neg_sort(lst):
    pos = iter(sorted([i for i in lst if i > 0]))
    return [next(pos) if i > 0 else i for i in lst]

