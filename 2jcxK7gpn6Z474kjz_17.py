
# SOLUTION WITHOUT REGEX!!!
​
def security(txt):
    
    a, x, T, G, S = [], [], [], [], []
    
    for i in txt: 
        if i != "x": a.append(i)
    
    for i in range(len(a)):
        if a[i]=="T": T.append(i)
        elif a[i]=="G": G.append(i)    
        elif a[i]=="$": S.append(i)    
    
    if len(T) == 0 or len(S)==0: return "Safe"
​
    for i in T:
        for j in S:
            if abs(i-j) == 1: return "ALARM!"
​
    return "Safe"

