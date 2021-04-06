
def map_letters(word):
    if word=='':return {}
    s = list(set(list(word)))
    s.sort(key=lambda x:word.index(x))
    res = []
    obj={}
    for char in s:
        for i,match in enumerate(word):
            if char==match:
                res.append(i)
        obj[char] = res
        res =[]
    return obj

