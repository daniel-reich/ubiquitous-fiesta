
def sudoku_validator(x):
    lists = [i for i in x]
    for j in range(len(x)):
        lst = [x[i][j] for i in range(len(x))]
        lists.append(lst)
    
    for a in range(0,len(x),len(x)//3):
        for i in range(0,len(x),len(x)//3):
            lst = []
            for j in x[i:i+3]:
                lst.append(j[a:a+3])
            lists.append([item for sublist in lst for item in sublist]) # flattens lists of lists to one list and appends flattened list
   
    if list(filter(lambda lst: sorted(lst) != list(range(1,10)),lists)) == []:
        return True
    else:
        return False

