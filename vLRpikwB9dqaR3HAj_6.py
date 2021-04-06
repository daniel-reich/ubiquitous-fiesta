
def is_ord_sub(smlst, bglst):    
    indices = [(a, b) for a, b in enumerate(bglst)]
    loc = []
    g = -1
    x = 0
    for i in smlst:
        for j in range(x, len(indices)):            
            if i == indices[j][1]:
                if indices[j][0] > g:
                    loc.append(indices[j][0])
                    g = indices[j][0]
                    x += 1
                    break                        
​
    return len(loc) == len(smlst)

