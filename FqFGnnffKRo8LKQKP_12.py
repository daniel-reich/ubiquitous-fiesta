
def simple_numbers(a, b):
    res = [ ]
    for i in range(a,b+1):
        if sum([int(v)**int(j+1) for j,v in enumerate(list(str(i)))])==i:res.append(i)
    return res

