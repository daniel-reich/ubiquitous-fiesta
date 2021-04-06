
def flatten(r):
    flattened = []
​
    for e in r:
        if isinstance(e, list):
            flattened += flatten(e)
        else:
            flattened += [e]
​
    return flattened

