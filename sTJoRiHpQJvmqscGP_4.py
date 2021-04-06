
def daily_streak(lst):
    l = 0
    c = 0
    for i in lst:
        if i == True:
            c += 1
        else:
            l = max(l,c)
            c = 0
    return max(l,c)

