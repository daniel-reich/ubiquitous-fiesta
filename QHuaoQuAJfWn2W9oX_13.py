
def check_board(col, row):
    col_dict = {'a' : 0, 'b' : 1, 'c': 2,'d' : 3, 'e' : 4, 'f': 5, 'g' : 6, 'h' : 7}
    row_dict = {1: 7, 2 : 6, 3: 5, 4 :4, 5 : 3, 6: 2, 7 : 1, 8 : 0}
​
​
    new_col = col_dict[col]
    new_row = row_dict[row]
​
    rows = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]
​
    
    index = 0
    for i in rows:
        for j in range(8):
            rows[index][j] = validate_bishop(new_row,new_col,index,j) or validate_rook(new_row,new_col,index,j)
        index = index + 1
​
    rows[new_row][new_col] = 0
    return rows
​
def validate_bishop(current_row,current_column, target_row,target_column):
​
        if abs(current_column - target_column)  != abs(target_row - current_row):
            return False
​
        return True
​
​
​
def validate_rook(current_row,current_column, target_row,target_column):
​
        if current_column == target_column or current_row == target_row:
            return True
​
        return False

