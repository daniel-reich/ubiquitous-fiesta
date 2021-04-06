
def is_mini_sudoku(square): 
    num = []
    
    for n in square:
        for x in n:
            if x == 0:
                return False
    
    for n in square:
        for x in n:
            if x in num:
                return False
            else:
                num.append(x)             
​
    return True

