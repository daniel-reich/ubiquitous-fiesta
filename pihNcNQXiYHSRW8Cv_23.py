
def sort_by_length(lst):
    for x in range(len(lst)):
        minimum = x
        for y in range(x+1,len(lst)):
            if len(lst[x])>len(lst[y]):
                minimum = y
        lst[x],lst[minimum] = lst[minimum], lst[x]
    return lst

