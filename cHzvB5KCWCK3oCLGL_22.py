
def game_of_life(board):
    # put wall of 0's around board
    b = []
    top = [0]*(2+len(board[0]))
    b.append(top)
    for row in board:
        b.append([0] + row + [0])
    b.append(top)
​
    loa = []
    for r in range(1, 1+len(board)):
        a = ''
        for c in range(1, 1+len(board[0])):
            a += get_new(b, r, c)
        loa.append(a)
    return '\n'.join(loa)
​
def get_new(b, r, c):
    cnt = 0
    rr = r-1
    for cc in [c-1, c, c+1]:
        if b[rr][cc] == 1:
            cnt +=1
    rr = r+1
    for cc in [c-1, c, c+1]:
        if b[rr][cc] == 1:
            cnt +=1
    rr = r
    for cc in [c-1, c+1]:
        if b[rr][cc] == 1:
            cnt +=1
    if b[r][c] == 1:
        if cnt in (0, 1, 4, 5, 6, 7, 8):
            return '_'
        else:
            return 'I'
    if cnt == 3:
        return 'I'
    return '_'

