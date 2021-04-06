
def move(mat):
    def movement(direction):
        if direction == 'up':    
            return move(mat[1:] + mat[:1])
        if direction == 'down':  
            return move(mat[-1:] + mat[:-1])
        if direction == 'left':  
            return move([i[1:] + i[:1] for i in mat])
        if direction == 'right': 
            return move([i[-1:] + i[:-1] for i in mat])
        return mat
    return movement

