
def iqr(lst):
    l, lst = len(lst), sorted(lst)
    return median(lst[(l+1)//2:]) - median(lst[:l//2])
​
def median(lst):
    l = len(lst)
    return sum(lst[(l-1)//2 : l//2 +1])/len(lst[(l-1)//2: l//2 +1])

