
from collections import deque
​
def knight_bfs(a, b, c, d):
    dd = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2,-1)]
​
    board = [[0 for j in range(8+4)] for i in range(8+4)]
    path = [[None for j in range(8+4)] for i in range(8+4)]
    
    for i in range(8+4):
        board[0][i] = -1
        board[1][i] = -1
        board[8+4-1][i] = -1
        board[8+4-2][i] = -1
        
        board[i][0] = -1
        board[i][1] = -1
        board[i][8+4-1] = -1
        board[i][8+4-2] = -1
        
    q = deque([(a+2-1, b+2-1)])
    while len(q) > 0:
        node = q.popleft()
        if node[0] == c+2-1 and node[1] == d+2-1:
            break
        
        for delta in dd:
            x = node[0] + delta[0]
            y = node[1] + delta[1]
            
            if board[x][y] >= 0:
                board[x][y] = board[node[0]][node[1]] + 1
                q.append((x,y))
    
    return board[c+2-1][d+2-1]

