
def classify_rug(pattern):
    vertical = all(x == x[::-1] for x in pattern)
    rotate  = [[x[i] for x in pattern] for i in range(len(pattern[0]))]
    horizontal = all(x == x[::-1] for x in rotate)
    classes = {(1,1):"perfect", (1,0):"vertically symmetric",
        (0,1):"horizontally symmetric", (0,0):"imperfect"}
    return classes[(vertical, horizontal)]

