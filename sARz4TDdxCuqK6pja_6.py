
def deadly_virus(persons, n):
    count = 0
    indexes = []
    for i in range(n):
        for j in range(len(persons)):
            for i in range(len(persons[i])):
                if persons[i][j] == 'V':
                    indexes.append((i,j))
        for x,y in indexes:
            try:
                ##above
                if x-1 == -1:
                    pass
                else:
                    persons[x-1][y] = 'V'
            except IndexError as err:
                pass
            try:
                ##below
                persons[x+1][y] = 'V'
            except IndexError as err:
                pass
            try:
                ##left
                if y-1 == -1:
                    pass
                else:
                    persons[x][y-1] = 'V'
            except IndexError as err:
                pass
            try:
                ##right
                indexes = []
                persons[x][y+1] = 'V'
            except IndexError as err:
                pass
    return persons

