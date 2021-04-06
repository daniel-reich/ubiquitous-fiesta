
def iso_group(lst):
    mx=max(lst)
    c=0
    for i in lst:
        if i==mx:
            c+=1
    if c==1:
        return mx
    else:
        return [mx]*c

