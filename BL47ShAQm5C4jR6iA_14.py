
def third_most_expensive(dct):
    if len(dct) > 2:
        lst = sorted([(v, k) for k, v in dct.items()], reverse=True)
        return lst[2][1]
    return False

