
def num_split(num):
    r = []
    if num < 0:
        neg = "-"
    else:
        neg = ""
    num = abs(num)
    for i in range(len(str(num))):
        add = neg + str(num)[i] + "0" * (len(str(num)) - i - 1)
        r.append(int(add))
    return r

