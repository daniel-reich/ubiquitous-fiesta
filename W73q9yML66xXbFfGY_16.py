
def coloured_triangle(row):
    adict = {'BG': 'R', 'RG': 'B', 'BR': 'G'}
    if len(row) == 1:
        return row
    newlist = []
    first_row = list(row)
    new_row = ''
    increment = len(row)
    while increment != 0:
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                new_row += row[i]
            elif (row[i] + row[i+1]) in adict.keys():
                new_row += adict[row[i] + row[i+1]]
            elif (row[i+1] + row[i]) in adict.keys():
                new_row += adict[row[i+1] + row[i]]
        increment -= 1
        if len(new_row) == 1:
            break
        row = new_row
        new_row = ''
    return new_row

