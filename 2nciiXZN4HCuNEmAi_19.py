
def flatten(r):
    result = []
    for item in r:
        if type(item) != list:
            result.append(item)
        elif type(item) == list:
            result.extend(flatten(item))
    return result

