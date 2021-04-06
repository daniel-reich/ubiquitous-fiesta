
def str_to_dict(lst):
    d = {}
    for x in lst:
        k, v = x.split('=')
        d[k] = v
    return d

