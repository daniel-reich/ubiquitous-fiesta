
def bishop(start, end, n):
    board = [[(x+y)%2 for x in range(0, 8)] for y in range(0,8)]
    startCol = ord(start[0]) - 97
    startRow = (int(start[1])  + (8-int(start[1])) + (1-int(start[1])) )- 1
    endCol = ord(end[0]) - 97
    endRow = (int(end[1])  + (8-int(end[1])) + (1-int(end[1])) )- 1
    
    if start == end:
        return True
    elif n==0:
        return False
    elif board[startRow][startCol] != board[endRow][endCol]:
        return False
    elif n == 1:
        if abs(startCol - endCol) == abs(startRow - endRow):
            return True
        else:
            return False
    else:
        return True

