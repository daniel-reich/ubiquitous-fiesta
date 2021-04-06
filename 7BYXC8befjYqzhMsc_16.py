
def list_shape(lst):
    if type(lst[0]) is list:
        return(len(lst[0]), len(lst))
    else:
        return (len(lst), 1)
​
​
def classify_rug(pattern):
    horzSym = False
    vertSym = False
​
    dim = list_shape(pattern)
    # Check horizontal symmetry
    if dim[1] == 1:
        horzSym = True
    else:
        x = 0
        checking = True
        while x < dim[0] and checking:
            y = 0
            while y < dim[1]/2 and checking:
                if pattern[y][x] != pattern[dim[1] - y - 1][x]:
                    checking = False
                    horzSym = False
                    break
                else:
                    horzSym = True
                y += 1
            x += 1
​
    # Check vertical symmetry
    if dim[0] == 1:
        vertSym = True
    else:
        y = 0
        checking = True
        while y < dim[1] and checking:
            x = 0
            while x < dim[0] / 2 and checking:
                if pattern[y][x] != pattern[y][dim[0] - x - 1]:
                    checking = False
                    vertSym = False
                    break
                else:
                    vertSym = True
                x += 1
            y += 1
​
    # Classify based on results
    if horzSym and vertSym:
        return "perfect"
    elif horzSym:
        return "horizontally symmetric"
    elif vertSym:
        return "vertically symmetric"
    else:
        return "imperfect"

