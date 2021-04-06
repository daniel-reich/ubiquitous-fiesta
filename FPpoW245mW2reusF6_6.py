
def even_last(lst):
    if len(lst) == 0:
        return 0
    else:
        return sum([lst[i] for i in range(len(lst)) if i % 2 == 0]) * lst[-1]

