
def encryption(txt):
    tmp = ''
    txt = txt.replace(' ', '')
    rows = int(len(txt)**0.5)
    if len(txt)**0.5 % 1 > 0:
        cols = rows + 1
        if len(txt)**0.5 % 1 > 0.5:
            rows += 1
    else:
        cols = rows
    rest = cols*rows - len(txt)
    for i in range(cols - rest):
        for j in range(rows):
            tmp += txt[j*cols+i]
        if i != cols - 1: tmp += ' '
​
    for i in range(cols - rest, cols):
        for j in range(rows -1):
            tmp += txt[j*cols+i]
        if i != cols - 1: tmp += ' '
    return tmp

