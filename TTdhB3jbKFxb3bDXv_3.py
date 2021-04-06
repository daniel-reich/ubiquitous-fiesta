
def left_shift(alist,i):
    if i == 0:
        return alist
    elif i < len(alist):
        return alist[i:] + alist[:i]
    else:
        while True:
            i= abs(len(alist)-i)
            if i >= len(alist):
                continue
            return alist[i:] + alist[:i]
​
​
​
def right_shift(alist,i):
    if i == 0:
        return alist
    elif i < len(alist):
        return alist[-i:] + alist[:-i]
    else:
        while True:
            i= abs(len(alist)-i)
            if i >= len(alist):
                continue
            return alist[i:] + alist[:-i]

