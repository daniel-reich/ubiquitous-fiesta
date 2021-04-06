
def split_bunches(bunches):
    res = []
    for b in bunches:
        print (b.items())
        q = b["quantity"]
        while q >= 1:
            res.append({'name': b['name'], "quantity": 1})
            q -= 1
    return res

