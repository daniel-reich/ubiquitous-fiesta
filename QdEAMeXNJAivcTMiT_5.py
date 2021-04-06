
def boxes(weights):
    box, count = 0, weights[0]
    for x in weights[1:]:
        if x + count > 10:
            box += 1
            count = 0
        count += x
    return box + 1

