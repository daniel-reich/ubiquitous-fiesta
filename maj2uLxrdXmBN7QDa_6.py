
def bishop(start, end, n):
    if start == end:
        return True
    if n == 0:
        return False
    d = {"a": 1, "b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    if n > 1:
        return (d[start[0]]+int(start[1])+d[end[0]]+int(end[1]))%2 == 0
    if n == 1:
        return d[start[0]]+int(start[1])==d[end[0]]+int(end[1]) or d[start[0]]+8-int(start[1])==d[end[0]]+8-int(end[1])

