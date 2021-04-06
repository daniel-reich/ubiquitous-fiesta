
def sudoku_validator(bo):
    for row in range(9):
        if not sum(bo[row]) == 45:
            return False
    
    for col in range(9):
        if not sum(list(zip(*bo))[col]) == 45:
            return False
    
    list_box =[0, 3, 6]
    new_list = []
    for x in list_box:
        for num in list_box:
            for i in range(x,x+3):
                for j in range (num, num + 3):
                     new_list.append(bo[i][j])
    data = [new_list[t:t+9] for t in range(0,len(new_list),9)]
    for n in range(9):
        if not sum(data[n]) == 45:
            return False
                        
    return True

