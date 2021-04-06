
def shadow_sentence(a, b):
    if len(a.split()) != len(b.split()):
        return False
​
    for x, y in zip(a.split(), b.split()):
        if len(x) != len(y) or len(set(x) & set(y)) >= 1:
            return False
​
    return True

