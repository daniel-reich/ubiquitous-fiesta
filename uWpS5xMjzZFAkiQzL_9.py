
def odds_vs_evens(num):
    res = [int(x) for x in str(num)]
    odds=[]
    evens=[]
    for i in res:
        if i %2==0:
            evens.append(i)
        else:
            odds.append(i)
    if sum(odds)>sum(evens):
        return('odd')
    elif sum(odds)==sum(evens):
        return('equal')
    else:
        return('even')

