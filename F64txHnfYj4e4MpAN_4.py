
def schoty(frame):
    lst = []
    for i in frame:
        line = [x for x in i]
        n = line.index('-')
        lst.append(str(n))
    return int(''.join(lst))

