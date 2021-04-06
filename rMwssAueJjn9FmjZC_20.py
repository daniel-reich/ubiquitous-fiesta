
def number_pairs(txt):
    res = list(map(lambda x:int(x), txt.split(' ')))[1:]
    a = list(set(res))
    i =0
    for j in a:
        i+=res.count(j)//2
    return i

