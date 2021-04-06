
def to_list(dct):
    result = []
    for key1 in dct:
        result.append([key1, dct[key1]])
    result.sort(key = lambda x : x[0])
    return result

