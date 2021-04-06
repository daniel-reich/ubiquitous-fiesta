
import numpy as np
​
def knight_bfs(x1,y1,x2,y2):
    steps = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
    board = np.ones((9,9),dtype=np.int16)*10000
    board[x1][y1] = 0
    work_list = []
    for i in range(1,9):
        for j in range(1,9):
            work_list.append([i, j])
    
    while(len(work_list) !=0):
        min_index = 0
        min_number = 10000
        for i,ele in enumerate(work_list):
            x = ele[0]
            y = ele[1]
            if board[x][y] < min_number:
                min_number = board[x][y]
                min_index = i
        x,y = work_list.pop(min_index)
        #print(x,y,board[x][y])
        for ele in steps:
            x_new = x + ele[0]
            y_new = y + ele[1]
            if (x_new >= 1 and x_new <=8) and (y_new >= 1 and y_new <=8):
                if board[x][y] + 1 <= board[x_new][y_new]:
                    board[x_new][y_new] = board[x][y] + 1
    
        
    return board[x2][y2]

