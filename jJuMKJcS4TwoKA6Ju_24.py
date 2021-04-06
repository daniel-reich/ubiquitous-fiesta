
def dial(txt):
    lok = list('abcdefghijklmnopqrstuvwxyz')
    lov = list('22233344455566677778889999')
    d = dict(zip(lok, lov))
    return ''.join([d[x.lower()] if x.lower() in d else x
                 for x in txt])

