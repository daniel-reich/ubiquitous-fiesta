
def swap_dict(dic):
    sd = {}
    for k, v in dic.items():
        nv = sd.get(v, [])
        nv.append(k)
        sd[v] = nv
    return sd

