
def who_won(board):
    transpose = transposes(board)
    row_wise = return_winner(board)
    column_wise = return_winner(transpose)
    diagnol_wise = diagnol_winner(board)
    if row_wise is not None:
        return(row_wise)
    #column_wise = return_winner(transpose)
    elif column_wise is not None:
        return(column_wise)
    elif diagnol_wise is not None:
        return(diagnol_wise)
        
        
def equal(arr):
    if (all(x == y for x, y in zip(arr, arr[1:]))):
        return(arr[0])
    
def return_winner(board):
    a = [each for each in board if equal(each) is not None]
    if len(a) != 0:
        return(a[0][0])
​
def transposes(y):
    transpose = list(zip(*y))
    transpose = [list(ele) for ele in transpose]
    return(transpose)
​
​
def diagnol_winner(board):
    lst = [row[i] for i, row in enumerate(board)]
    lst1 = [row[i] for i, row in enumerate(board[::-1])]
    if equal(lst) is not None:
        return(equal(lst))
    elif equal(lst1) is not None:
        return(equal(lst1))

