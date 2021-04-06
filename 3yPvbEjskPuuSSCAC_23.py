
def trimmed_averages(lst):
    lst=sorted(lst)[1:-1]
    return round(sum(lst)/len(lst))

