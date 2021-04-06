
def identify(*cube):
    if max([len(x) for x in cube]) == len(cube) \
            and min([len(x) for x in cube]) == len(cube):
        return 'Full'
    elif max([len(x) for x in cube]) > len(cube) and min([len(x) for x in cube])\
            ==max([len(x) for x in cube]):
        return 'Non-Full'
    elif max([len(x) for x in cube]) != min([len(x) for x in cube]):
​
        return 'Missing {}'.format(max([len(x) for x in cube]) * len(cube) -
                                   len([x for y in cube for x in y]))

