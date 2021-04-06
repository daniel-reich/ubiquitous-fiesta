
def subtract_matrix(lst1, lst2):
    myans = []
    for y in range(len(lst1)):
        temp = []
        for x in range(len(lst2)):
            temp.append(float(lst1[y][x])-float(lst2[y][x]))
        myans.append(temp)
    return myans

