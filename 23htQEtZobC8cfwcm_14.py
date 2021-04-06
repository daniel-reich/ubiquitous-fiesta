
def canConcatenate(lst, target):
    ll = []
    for i in lst:
        for x in i:
            if x in target:
                ll.append(x)
            l = sorted(ll)
​
    if l[::-1] == sorted(target) or l == sorted(target):
        return True
    else:
        return False

