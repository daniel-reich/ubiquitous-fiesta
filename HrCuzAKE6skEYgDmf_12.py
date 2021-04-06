
def pairs(lst):
    res = []
    if len(lst)%2 !=0:
        for i in range((len(lst)//2)+1):
            a = [lst[i],lst[-(i+1)]]
            res.append(a)
        return res
    res = []
    if len(lst)%2 ==0:
        for i in range((len(lst))//2):
            a = [lst[i],lst[-(i+1)]]
            res.append(a)
        return res
    else:
        return []

