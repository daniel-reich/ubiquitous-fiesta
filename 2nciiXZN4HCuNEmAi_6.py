
def flatten(r, resp=None, a="main"):
    if resp is None: 
        resp = list()
    if type(r) == list:
        for i in r:
            resp.append(flatten(i, resp, "rec"))
    else: 
        return r
    return resp if a== "rec" else [i for i in resp if type(i)!=list]

