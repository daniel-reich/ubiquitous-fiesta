
def third_most_expensive(dct):
    import operator
    if len(dct) < 3:
        return False
    else:
        x = sorted(dct.items(), key = operator.itemgetter(1))
        return x[-3][0]

