
def make_anagram(a, b):
    if len(a)>len(b):       
        large = sorted(a)
        small = sorted(b)
    else:
        large = sorted(b)
        small = sorted(a)
    res=[]                      
    for i in range(len(large)):
        if large[i] in small:
            small.remove(large[i])
            res.append(large[i])
    return ((len(large)-len(res))+len(small))

