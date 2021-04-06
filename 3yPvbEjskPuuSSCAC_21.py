
def trimmed_averages(lst):
    tot = sum(lst) - max(lst) -min(lst)
    return round(tot/(len(lst)-2))

