
def missing(lst):
    gap = []
    for i, x in enumerate(lst):
        if i != len(lst) - 1:
            gap.append(lst[i+1] - x)
    index_gap = gap.index(max(gap))
    correct_gap = min(gap)
    return lst[index_gap] + correct_gap

