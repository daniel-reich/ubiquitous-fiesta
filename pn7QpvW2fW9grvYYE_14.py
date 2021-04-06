
def find_fulcrum(lst):
    for i in range(1,len(lst)):
        if sum(lst[:i])==sum(lst[i+1:]):
            return lst[i]
            break
    return -1

