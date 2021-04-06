
def numbers_to_ranges(lst):
    
    rangeIdx=0
    
    if lst==[]:
        return []
    
    else:
        ranges=[[lst[0],lst[0]]]
        for i in lst:
            if ranges[rangeIdx][1] in (i,i-1):
                ranges[rangeIdx][1]=i
            else:
                ranges.append([i,i])
                rangeIdx+=1
    return (','.join(map(lambda p:'%s-%s'%tuple(p) if p[0]!=p[1] else str(p[0]),ranges ))).split(',')

