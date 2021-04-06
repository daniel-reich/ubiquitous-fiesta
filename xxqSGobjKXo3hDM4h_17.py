
def ing_extractor(string):
    x=[]
    lst=string.split()
    if len(lst)==1:
        return []
    for word in lst:
        if len(word)>5 and (word[-3:]=='ing'or word[-3:]=='ING'):
             x.append(word)
    return x

