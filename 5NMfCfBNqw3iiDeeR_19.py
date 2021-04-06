
def sum_minimums(lst):
    myans = 0
    for i in range(len(lst)):
        myans += min(lst[i])
​
    return myans

