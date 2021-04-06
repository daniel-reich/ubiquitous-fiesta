
def hex_distance(lst):
    lst = [list(x) for x in lst]
    a, b = [(x,y) for x in range(len(lst)) for y in range(len(lst[x])) if lst[x][y] == 'x']
​
    if min(b) == b[0]:
        first = min(b) - a[0]
        last = ((b[1] - (a[1] + first)) // 2)
        return first + last if last >= 0 else first
    else:
        first = b[0] - a[0]
        last = (a[1] - first) // 2
        return first + last if last >= 0 else first

