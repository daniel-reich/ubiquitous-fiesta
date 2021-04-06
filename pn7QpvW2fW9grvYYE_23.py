
def find_fulcrum(lst):
    l = []
    
    for i in range(len(lst)):
        if sum(lst[0:i+1]) == sum(lst[i:]):
            return lst[i]
    return -1

