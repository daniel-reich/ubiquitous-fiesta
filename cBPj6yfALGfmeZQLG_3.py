
def vertical_txt(txt):
    lst = txt.split()
    mx = len(max(lst, key = lambda x: len(x)))
    print(lst, mx)
​
    tbl = [[' ' for i in range(len(lst))] for j in range(mx)]
    print(tbl)
​
    col = 0
    for wd in lst:
        for row in range(len(wd)):
            tbl[row][col] = wd[row]
        col += 1
​
    return tbl

