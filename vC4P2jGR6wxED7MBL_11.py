
def larger_than_right(lst):
    return [n for i, n in enumerate(lst[:-1]) if n > max(lst[i+1:])] + [lst[-1]]

