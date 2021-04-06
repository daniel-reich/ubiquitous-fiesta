
def is_checkerboard(lst):
    i = 1
    while i <= len(lst) - 1:
        if i == len(lst) - 1:
            for j in range(len(lst[i])):
                if (lst[i][j] == 0 and lst[i-1][j] != 1) or (lst[i][j] == 1 and lst[i-1][j] != 0):
                    return False
        else:
            for j in range(len(lst[i])):
                if (lst[i][j] == 0 and lst[i-1][j] != 1) or (lst[i][j] == 1 and lst[i-1][j] != 0) or (lst[i][j] == 0 and lst[i+1][j] != 1) or (lst[i][j] == 1 and lst[i+1][j] != 0):
                    return False
        i += 2
    return True

