
def quad_sequence(lst):
    difference = lst[-1] - lst[-2]  
    constant = difference - (lst[-2] - lst[-3])
    res = [lst[-1]]
    
    for _ in range(len(lst)):
        difference += constant
        res.append(res[-1] + difference)
​
    return res[1:]

