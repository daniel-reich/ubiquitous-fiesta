
def floyd(up_to = None, n_row = None):
    ans = []
    start , i = 1 , 1
    par = True
    while par:
        ans.append([j for j in range(start,start+i)])
        start += i
        i += 1
        if up_to in ans[-1]:
            par = False
        if i - 1 == n_row:
            par = False
    return ans

