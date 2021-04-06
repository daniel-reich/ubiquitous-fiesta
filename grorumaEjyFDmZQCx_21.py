
def check_horizontal(lst):
    for i in lst:
        if len(set(i)) != 1:
            return False
    return True
​
def check_vertical(lst):
    for i in range(0,len(lst[0])):
        vertical = []
        for y in range(len(lst)):
            vertical.append(lst[y][i])
        if len(set(vertical)) != 1:
            return False
    return True
        
def check_diagonal_right(lst):
    for i in range(0,len(lst)):
        for y in range(0,len(lst[i])):
            if i > 0 and i < len(lst)-1 and y == 0:
                if lst[i][y] != lst[i-1][y+1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y == len(lst[i])-1:
                if lst[i][y] != lst[i+1][y-1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y > 0 and y < len(lst[i])-1:
                if lst[i][y] != lst[i-1][y+1] or lst[i][y] != lst[i+1][y-1]:
                    return False
    return True
​
def check_diagonal_left(lst):
    for i in range(0,len(lst)):
        for y in range(0,len(lst[i])):
            if i > 0 and i < len(lst)-1 and y == 0:
                if lst[i][y] != lst[i+1][y+1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y == len(lst[i])-1:
                if lst[i][y] != lst[i-1][y-1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y > 0 and y < len(lst[i])-1:
                if lst[i][y] != lst[i-1][y-1] or lst[i][y] != lst[i+1][y+1]:
                    return False
    return True
​
def is_wristband(lst):
    return check_horizontal(lst) or check_vertical(lst) or check_diagonal_left(lst) or check_diagonal_right(lst)

