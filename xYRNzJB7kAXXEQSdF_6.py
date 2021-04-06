
def wiggle_string(s):
    a = []
    for i in range(len(s)+1):
        a.append(" " * i + s)
    for i in range(len(s)-1, -1, -1):
        a.append(" " * i + s)
    return a

