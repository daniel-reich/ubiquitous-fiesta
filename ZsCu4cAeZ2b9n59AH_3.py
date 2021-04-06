
def lost_dog(*args, n=0):
    res = dict()
    for r, row in enumerate(args):
        if 0 in row:
            n += 1
            res["Dog{}".format(n)] = ("House ({}) and Room ({})"
                                      .format(r + 1, row.index(0) + 1))
    return res if n else "Dog not found!"

