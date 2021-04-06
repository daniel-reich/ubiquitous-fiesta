
def can_exit(lst, row=0, col=0):
    row_last = len(lst) - 1
    col_last = len(lst[0]) - 1
    cell_value = lst[row][col]
    wall = 1 #blocked cell
    visited = 3 #visited cell 
    if row == row_last and \
       col == col_last and \
       cell_value != wall:
        return True
    elif cell_value == wall or cell_value == visited: 
        return False
    lst[row][col] = 3 # mark as visited 
    #explore neighbours 
    if (row < row_last and can_exit(lst, row+1, col))\
        or (row > 0 and can_exit(lst, row - 1, col))\
        or (col < col_last and can_exit(lst, row, col + 1))\
        or (col > 0 and can_exit(lst, row, col - 1)):
        return True
    return False

