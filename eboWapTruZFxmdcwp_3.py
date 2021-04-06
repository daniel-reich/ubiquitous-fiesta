
def is_positive_dominant(lst):
    pos = sum([1 for i in set(lst) if i > 0])
    neg = sum([1 for i in set(lst) if i < 0])
    return pos > neg

