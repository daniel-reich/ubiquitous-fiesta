
def crop_hydrated(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 'c':
                if 0 == sum([field[row][col] == 'w' for row in range(i-1, i+2)for col in range(j-1, j+2)
                            if 0 <= row < len(field) and 0 <= col < len(field[0])]):
                    return False
    return True

