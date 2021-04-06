
def can_move(piece, current, target):
    rook = {pos for dist in range(-8,9)
                for pos in [(0, dist), (dist, 0)]}
    bishop = {pos for dist in range(-8,9)
                for pos in [(dist, dist), (dist, -dist)]}
    moves = {'Pawn': {(0,1)},
             'King': {(col, row) for col in [-1,0,1] for row in [-1,0,1]},
             'Knight': {(col,  row) for row in [-2,-1,1,2]
                        for col in [-2,-1,1,2] if abs(col)!=abs(row)},
             'Bishop': bishop, 'Rook': rook, 'Queen': bishop | rook}
    
    (c1,r1),(c2,r2) = current,target
    move = ord(c2)-ord(c1), ord(r2)-ord(r1) 
    return move in moves[piece]

