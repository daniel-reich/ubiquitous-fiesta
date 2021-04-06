
def freq_count(lst, el, depth=0, count=(0,0)):
    if type(count)==tuple:
        count=[list(count)]
    if len(count)-1<depth:
        count.append([depth,0])
    for item in lst:
        if type(item)==int:
            if item==el:
                count[depth][1]+=1
        else:
            depth+=1
            freq_count(item,el,depth,count)
            depth-=1
    return count

