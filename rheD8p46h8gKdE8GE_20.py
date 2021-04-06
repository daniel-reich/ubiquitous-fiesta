
def clip_value(v):
    return min(255,max(0,v))
    
def grayout(v):
    v = map(clip_value,v)
    a = round(sum(v) / 3)
    return [a, a, a]
​
def grayoutline(l):
    return list(map(grayout,l))
​
def grayscale(lst):
    return list(map(grayoutline,lst))

