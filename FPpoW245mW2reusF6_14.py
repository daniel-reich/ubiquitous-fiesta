
def even_last(lst):
    count = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            count += lst[i]
    if lst:
        return count * lst[-1]
    elif not lst:
        return 0

