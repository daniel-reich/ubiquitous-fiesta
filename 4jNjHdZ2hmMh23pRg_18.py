
def cutting_grass(lst, *cuts):
    l = []
    for x, y in enumerate(cuts):
        for a, b in enumerate(lst):
            lst[a] = b - y
           
            if lst[a] <= 0:
                for j in cuts[x:]:
                    l.append("Done")
                return l
        
        l.append(lst[::])
        
    return l

