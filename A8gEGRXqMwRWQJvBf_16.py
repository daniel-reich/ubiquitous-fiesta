
def tic_tac_toe(board):
    fdiag = []
    rdiag = []
    for i in range(len(board)):
        
        row = board[i]
        #if rows are same value
        if all(val == row[0] for val in row):
            return row[0]
        
        #calculate column
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
            
            #front diagonal is where i=j
            if i == j:
                fdiag.append(board[j][i])
                
                #reverse diagonal middle case
                if i == 1:
                    rdiag.append(board[j][i])
            #reverse diagonal other cases
            if (j == 0 and i == 2) or (j == 2 and i == 0):
                rdiag.append(board[j][i])
                
        #if col is the same
        if all(val == col[0] for val in col):
            return col[0]
        
    #if front diagonal is same
    if all(val == fdiag[0] for val in fdiag):
        return fdiag[0]
    #if reverse diagonal is same
    if all(val == rdiag[0] for val in rdiag):
        return rdiag[0]
        
    return 'Draw'

