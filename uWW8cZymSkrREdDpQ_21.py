
def sums_up(lst):
    ans = []
    for k,i in enumerate(lst):
        for l,j in enumerate(lst[k+1:]):
            if j + i == 8:
                ans.append([i,j,l+k])
    ans = sorted(ans,key=lambda x:x[2])
    return {'pairs':[sorted(i[:2]) for i in ans]}

