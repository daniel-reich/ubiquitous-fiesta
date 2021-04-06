
def trimmed_averages(lst):
    lst.pop(lst.index(max(lst)))
    lst.pop(lst.index(min(lst)))
    return round(sum(lst)/len(lst))

