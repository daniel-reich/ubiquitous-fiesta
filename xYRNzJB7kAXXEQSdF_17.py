
def wiggle_string(s):
    x = (list(range(len(s)+1)) + list(range(len(s)-1,-1,-1)))
    return [' '*i + s for i in x]

