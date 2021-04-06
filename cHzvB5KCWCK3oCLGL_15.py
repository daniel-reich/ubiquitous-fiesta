
def neighbours(arr, x, y):
    empty = populated = 0
    # locations outside the bounds of the array are dicarded by the filter operation
    for r,c in filter(lambda t: 0<=t[0]<len(arr) and 0<=t[1]<len(arr[0]), [(a,b) for a, b in [(x-1, y-1), (x, y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]]):
        if arr[r][c] == 0:
            empty += 1
        elif arr[r][c] == 1:
            populated += 1
    return (empty, populated)        
​
def game_of_life(board):
    nextgen = [['_' for _ in range(len(board[0]))] for _ in range(len(board))]
    for row in range(len(board)):
        for col in range(len(board[0])):
            e, p = neighbours(board, row, col)
            if (board[row][col] == 0 and p == 3) or (board[row][col] == 1 and 2 <= p <= 3):
                nextgen[row][col] = 'I'
    res = '\n'.join([''.join(row) for row in nextgen])
    return res

