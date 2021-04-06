
def check_pattern(lst, pattern):
    lst = [tuple(x) for x in lst]
    dic = {key : value for key, value in zip(pattern, lst)}
    lst = [x for x in zip(pattern, lst)]
    one = all([lst[i][1] == dic[lst[i][0]] for i in range (len(pattern))])
    two = len(dic.values()) == len(set([value for value in dic.values()]))
    return one and two

