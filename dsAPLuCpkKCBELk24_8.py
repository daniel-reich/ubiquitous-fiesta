
def get_products(x):
    lst = []
    for i,j in enumerate(x):
        a = [str(v) for v in x if v!=x[i]]
        lst.append(eval("*".join(a)))
    return lst

