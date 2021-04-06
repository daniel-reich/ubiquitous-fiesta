
def is_mini_sudoku(sq):
    total = []
    for elem in sq:
        for i in elem:
            total.append(i)
        
        
    total.sort()
    count = 1
    if count == total[0]:
        for elem in total:
            count += 1
            if elem + 1 == count:
                pass
            else:
                return False
    else:
        return False
    
    return True

