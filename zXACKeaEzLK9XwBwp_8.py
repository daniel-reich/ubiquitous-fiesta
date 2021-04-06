
def split_bunches(bunches):
    x,y=[],[]
    for i in bunches:
        for j,v in i.items():
            if type(v)==int:
                for m in range(v):
                    i.update({"quantity": 1})
                    x.append(i)
    return x

