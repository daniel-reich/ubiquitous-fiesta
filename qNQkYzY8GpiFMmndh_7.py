
def join(lst,s='',temp=10):
    if len(lst) == 0:
        return [s, temp]
    else:
        l = len(s)
        while l > 0:
            l -= 1
            if s[l:] not in lst[0] and s[l+1:] in lst[0]:
                if temp > len(s[l+1:]): temp = len(s[l+1:]) 
                break
        s += lst[0][len(s[l+1:]):]
        return join(lst[1:],s,temp)

