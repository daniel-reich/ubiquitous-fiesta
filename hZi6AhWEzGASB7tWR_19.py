
def check(lst):
    lst2=["increasing" if lst[x]<(lst[x+1]) else('decreasing' if lst[x]>(lst[x+1]) else 'neither') for x in range(len(lst)-1)]
    return list(set((lst2)))[0] if len(set((lst2)))==1 else 'neither'

