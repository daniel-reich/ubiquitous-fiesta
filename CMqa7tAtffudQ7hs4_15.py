
def sortList(lst, dex, output):
    
    for a in range(dex, len(lst)):
        if lst[a] == min(lst[dex:]):
            lst[dex], lst[a]  = lst[a], lst[dex]
            output.append( (dex, a) )
            #print(lst)
    if lst != sorted(lst):
        return sortList(lst, dex + 1, output)
    else:
        return output
def sorting_steps(lst):
    return sortList(lst, 0, [])

