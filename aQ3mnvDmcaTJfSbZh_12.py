
def bw_transform(s):
    t = sorted(s[i:] + s[:i] for i in range(len(s)))  
    l = [r[-1:] for r in t]  
    return "".join(l)

