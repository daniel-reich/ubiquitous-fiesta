
def bitwise_index(lst):
    count = 0
    even = [0, 2, 4, 6, 8]
    r = []
    for i in lst:
        if int(str(i)[-1]) in even:
            add = [i, count]
            r.append(add)
        count += 1 
        
    if not r:
        return "No even integer found!"    
    
    big, ind = r[0][0], r[0][1]
    for j in r:
        if j[0] > big:
            big = j[0]
            ind = j[1]
    return {"@{} index {}".format(["odd", "even"][ind in even], ind) : big}

