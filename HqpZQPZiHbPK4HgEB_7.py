
import itertools
def maxmin(n):
    res=[n]
    n=list(str(n))
    for i in itertools.permutations(range(len(n)),2):        
        new_num=n[:]        
        new_num[int(i[0])]=n[int(i[1])]
        new_num[int(i[1])]=n[int(i[0])]
        if new_num[0]!="0":
            res.append(int("".join(new_num)))    
    return (max(res),min(res))

