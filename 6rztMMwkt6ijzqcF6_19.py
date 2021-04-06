
def is_repeated(s):
    temp = (s + s).find(s, 1, -1)
    res = None
    if temp != -1:
        res = s[:temp]
    return len(s.split(res))-1 if res!=None else False

