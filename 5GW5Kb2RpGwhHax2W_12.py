
def spiral_transposition(my_list):
    new_list = []
​
    rows = len(my_list)
    columns = len(my_list[0])
    row = 0
    col = 0
​
    horizontal = True
    add = True
​
    while(True):
        if horizontal == True:
            if add == True:
                for i in range(columns):
                    new_list.append(my_list[row][col])
                    col += 1
​
                col -= 1
                row += 1
​
            else:
                for i in range(columns):
                    new_list.append(my_list[row][col])
                    col -= 1
​
                col += 1
                row -= 1
​
            horizontal = not horizontal
​
            rows -= 1
            if rows == 0:
                return new_list
            
        else:
            if add == True:
                for i in range(rows):
                    new_list.append(my_list[row][col])
                    row += 1
​
                row -= 1
                col -= 1
​
                add = not add
​
            else:
                for i in range(rows):
                    new_list.append(my_list[row][col])
                    row -= 1
​
                row += 1
                col += 1
​
                add = not add
​
            horizontal = not horizontal
​
            columns -= 1
            if columns == 0:
                return new_list

