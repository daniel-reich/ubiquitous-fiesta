
import copy 
​
def dance(lst, p):
    
    p = 1 if p == 'men' else 0
    nl = copy.deepcopy(lst)
​
    for i in range(len(lst)):
        nl[i][p] = lst[(i+1) * -1  ][p]
​
    return nl

