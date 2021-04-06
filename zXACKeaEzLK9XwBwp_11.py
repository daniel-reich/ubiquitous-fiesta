
def split_bunches(bunches):
    res =[]
    nobj ={}
    for bunch in bunches:
        for i in range(bunch['quantity']):
            nobj['name'] = bunch["name"]
            nobj['quantity'] = 1
            res.append(nobj)
            nobj = {}
    return  res

