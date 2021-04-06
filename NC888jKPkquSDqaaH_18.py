
def clean_up(files, sort):
    from collections import OrderedDict
    d = OrderedDict()
    for f in files:
        sp = f.split('.')
        if sort == 'prefix':
            pf = sp[0]
            d.setdefault(pf, []).append(f)
        else:
            sf = sp[1]
            d.setdefault(sf, []).append(f)
​
    return list(d.values())

