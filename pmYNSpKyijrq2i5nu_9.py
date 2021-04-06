
import itertools
​
​
​
​
##sections = [2, 4, 7, 10, 13, 18, 24]
​
def darts_solver(sections, darts, target):
    x = itertools.combinations_with_replacement(sections, darts)
    
    y = sorted([sorted(i) for i in x if sum(i) == target])
​
    str_y = []
    for i in y:
        i = [str(x) for x in i]
        str_y.append('-'.join(i))
    return str_y

