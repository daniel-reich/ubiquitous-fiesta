
def sums_up(lst):
    x = []
​
    for a in range(1,len(lst)):
        for b in range(a):
            if lst[a]+lst[b] == 8:
                x.append(sorted([lst[a],lst[b]]))
​
    dict = {'pairs':x}
    return dict

