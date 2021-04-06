
def firstRepeatedChar(str):  
    h = {}  
    for ch in str: 
        if ch in h: 
            return ch 
        else: 
            h[ch] = 0  
    return '\0'
def recur_index(txt):
    y=[]
    if txt==None:
        return {}
    x=firstRepeatedChar(txt)
    for i,v in enumerate(txt):
        if v==x:
            y.append([v,i])
    if len(y)==0:
        return {}
    return {y[0][0]:[y[0][1],y[1][1]]}

