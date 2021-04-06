
def find_broken_keys(txt1, txt2):
    result = []
    [result.append(c1) for c1, c2 in zip(txt1, txt2) if c1 != c2 and c1 not in result]
    return result

