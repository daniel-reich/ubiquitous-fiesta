
def spiral_order(arr):
    d = ['R', 'D', 'L', 'U']
    res = []
    
    while arr:
        if d[0] == 'R':
            res += arr.pop(0)
        elif d[0] == 'D':
            res += [i.pop() for i in arr]
        elif d[0] == 'L':
            res += arr.pop()[::-1]
        else:
            res += [i.pop(0) for i in arr][::-1]
        d = d[1:] + d[:1]
    return res

