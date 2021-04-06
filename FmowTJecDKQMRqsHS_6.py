
def crop_hydrated(x, c=1):
    lst = [['c' for i in range(len(x[0]))] for j in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 'w':
                lst[i][j] = 'w'
                if j != len(x[0])-1:
                    lst[i][j+1] = 'w'
                if j != 0:
                    lst[i][j-1] = 'w'
    lst2 = [[0 for i in range(len(lst))] for j in range(len(lst[0]))]
    for i in range(len(lst2)):
        for j in range(len(lst2[0])):
            lst2[i][j] = lst[len(lst2[0])-j-1][i]
    if c == 2:
        for i in lst2:
            if 'c' in i:
                return False
        else:
            return True
    else:
        return crop_hydrated(lst2, c+1)

