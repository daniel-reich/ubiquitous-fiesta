
def num_then_char(lst):
    alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cnt = [len(i) for i in lst]
    num = sorted([str(j) for i in lst for j in i if type(j) == int or type(j) == float], key = float)
    let = sorted([j for i in lst for j in i if type(j) == str])
    idx = 0; res = []; aux = []
    for i in num+let:
        if len(aux) < cnt[idx]: aux.append(float(i) if '.' in i else i if i in alp else int(i))
        else: res.append(aux); aux = []; aux.append(float(i) if '.' in i else i if i in alp else int(i)); idx += 1
    res.append(aux)
    return res

