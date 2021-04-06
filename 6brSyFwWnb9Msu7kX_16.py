
def pos_neg_sort(lst):
    pos = sorted([x for x in lst if x > 0], reverse = True)
    return [pos.pop() if x > 0 else x for x in lst]

