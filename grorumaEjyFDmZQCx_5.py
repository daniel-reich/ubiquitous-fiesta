
# note: I like working with rows rather than columns
#       hence all the transposing.
def is_wristband(lst):
    if test_rows(lst):      return True
    tlst = map(list, zip(*lst))
    if test_rows(tlst):     return True
    s = slide(lst, -1)
    ts = map(list, zip(*s))
    if test_rows(ts):       return True
    s = slide(lst, 1)
    ts = map(list, zip(*s))
    if test_rows(ts):       return True
    return False
​
def test_rows(arr):
    for row in arr:
        if len(set(x for x in row if x)) != 1:
            return False
    return True
​
# create new array with input diagonal entris aligned
# in columns in output array based on value of di
def slide(arr, di):
    cols = len(arr[0]) + len(arr) - 1
    s = []
    if di == -1:
        i = cols - len(arr[0])
    else:
        i = 0
    for row in arr:
        r = [None] * cols
        r[i:i+len(row)] = row
        s.append(r)
        i += di
    return s

