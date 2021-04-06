
def combine(lst):
    i = 0
    res = {}
    while(i<=len(lst)-2):
        res[lst[i][0]] = [lst[i][2],lst[i+1][2]]
        i+=2
        
    return res

