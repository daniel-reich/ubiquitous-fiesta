
def even_last(lst):
    return sum(i * lst[-1] for i in lst[::2])

