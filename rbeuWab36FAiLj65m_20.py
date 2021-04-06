
def grouping(w):
    dic = {}
    for word in w:
        dic.setdefault(check(word), []).append(word)
    for s in dic:
        dic[s] = sorted(dic[s], key=str.casefold)
    return dic
    
def check(x):
    return sum([1 for i in x if i.isupper()])

