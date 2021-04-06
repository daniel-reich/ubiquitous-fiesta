
def find_fulcrum(lst):
    count=[]
    for i in range(0,len(lst)-1):
        if sum(lst[i:])==sum(lst[:i+1]):
            count.append(i)
    if len(count)==0:
        return -1
    else:
        return lst[count[0]]

