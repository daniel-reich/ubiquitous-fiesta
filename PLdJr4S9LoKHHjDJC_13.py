
def identify(*cube):
    if len(cube) == len(cube[0]) and len(set([len(i) for i in cube])) == 1:
        return "Full"
    elif len(cube) !=max([len(i) for i in cube]) and len(set([len(i) for i in cube])) == 1:
        return "Non-Full"
    return "Missing {}".format(len(cube)*max([len(i) for i in cube]) - sum([len(i) for i in cube]))

