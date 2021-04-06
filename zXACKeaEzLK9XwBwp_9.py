
def split_bunches(bunches):
    r = []
    for i in bunches:
        add = {"name" : i["name"], "quantity": 1}
        for t in range(i["quantity"]):
            r.append(add)
    return r

