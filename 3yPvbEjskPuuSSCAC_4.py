
def trimmed_averages(lst):
    sum = 0
    lst.remove(max(lst))
    lst.remove(min(lst))
    for i in lst:
        sum += i
    return round(sum / len(lst))

