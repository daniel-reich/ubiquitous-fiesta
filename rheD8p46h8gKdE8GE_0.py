
def grayscale(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            vals = [0 if v < 0 else 255 if v > 255 else v for v in lst[i][j]]
            lst[i][j] = [round(sum(vals)/3)] * 3
    return lst

