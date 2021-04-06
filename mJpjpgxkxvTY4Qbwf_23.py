
def bingo_check(board):    
    import numpy as np
    blist=["x","x","x","x","x"]
    for x in range(5):
            if list(np.array(board)[x,:])==blist:
                return True
            if list(np.array(board)[:,x])==blist:
                return True
            if list(np.diag(np.array(board)))==blist:
                return True
            if list(np.diag(np.fliplr(np.array(board))))==blist:
                return True
    return False

