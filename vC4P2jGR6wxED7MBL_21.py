
def larger_than_right(lst):
    return [v for k,v in enumerate(lst[0:-1], 1) if v > max(lst[k:])] + lst[-1:]

