
def crop_hydrated(field):
​
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == "c":
                field[i][j] = sum([1 for u in range(i-1, i+2) for v in range(j-1, j+2)\
                                if 0 <= u < len(field) and 0 <= v < len(field[i]) and field[u][v] == "w"])
​
    field = [x for each in field for x in each]
    return True if not 0 in field else False

