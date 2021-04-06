
class Cell:
​
    def __init__(self, x,y,dist=0):
        self.x = x
        self.y = y
        self.dist = dist
​
​
def inbounds(nx, ny):
​
    return 1 <= nx <= 8 and 1 <= ny <= 8
​
def knight_bfs(a, b, c, d):
    pos = Cell(a,b,0) 
    queue = [pos]
    visited = [pos]
    moves = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)]
​
    while queue:
        pos = queue.pop(0)
        neighbors = [(pos.x+x, pos.y+y) for x,y in moves if inbounds(pos.x+x, pos.y+y)]
        for neighbor in neighbors:
            if neighbor == (c,d):
                return pos.dist + 1
            
            if neighbor not in visited:
                visited.append(neighbor)
                q,w = neighbor
                queue.append(Cell(q,w, pos.dist+1))
                
    return pos.dist

