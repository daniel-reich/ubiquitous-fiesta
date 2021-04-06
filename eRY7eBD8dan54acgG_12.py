
def is_checkerboard(lst):
    while True:
        for i in range(len(lst)-1):
            for j in range(len(lst)-1):
                if lst[i][j] == lst[i][j+1] or lst[i][j] == lst[i+1][j] :
                    return False
        return True

