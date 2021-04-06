
def split_n_cases(txt, cases):
    res =[]
    l = len(txt)//cases
    if len(txt)%cases!=0:return ['Error']
    for i in range(0,len(txt),l):
        res.append(txt[i:i+l])
    return res

