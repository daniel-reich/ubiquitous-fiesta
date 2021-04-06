
def is_positive_dominant(lst):
    pos = 0
    neg = 0
    for i in list(set(lst)):
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    return pos > neg

