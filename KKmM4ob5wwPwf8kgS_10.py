
def get_frequencies(lst):
    if lst == []:
        return {}
    dic = {}
    for d in lst:
        if dic.get(d):
            dic[d] += 1
        else:
            dic[d] = 1    
    return dic

