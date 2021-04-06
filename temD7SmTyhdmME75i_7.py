
def to_boolean_list(word):
    import string
    d = {y: x for x, y in enumerate(string.ascii_lowercase, 1)}
    buf = [1 if d[x] % 2 else 0 for x in word if x in d]
    res = [True if x ==1 else False for x in buf]
    return res

