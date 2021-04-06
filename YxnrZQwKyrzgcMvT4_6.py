
def rotation(lst):
    r = []
    for i in range(0,len(lst)):
        row = []
        for y in range(0,len(lst[0])):
            row.append(lst[y][i])
        r.append(row[::-1])
    return r
​
def rotate_transform(lst, num):
    if num > 0:
        while num > 4:
            num -= 4
        for i in range(num):
            lst = rotation(lst)
        return lst
    else:
        while num < -4:
            num += 4
        num += 4
        for i in range(num):
            lst = rotation(lst)
        return lst

