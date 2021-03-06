
knight_moves = ((0, 3, 2, 3, 2, 3, 4, 5),
                (3, 2, 1, 2, 3, 4, 3, 4),
                (2, 1, 4, 3, 2, 3, 4, 5),
                (3, 2, 3, 2, 3, 4, 3, 4),
                (2, 3, 2, 3, 4, 3, 4, 5),
                (3, 4, 3, 4, 3, 4, 5, 4),
                (4, 3, 4, 3, 4, 5, 4, 5),
                (5, 4, 5, 4, 5, 4, 5, 6))
​
def knight_bfs(a, b, c, d): 
    if (a,b,c,d) in [(8,1,7,2),(7,2,8,1),(8,8,7,7),(7,7,8,8),(1,1,2,2),(2,2,1,1),(1,8,2,7),(2,7,1,8)]:  
        return 4
    return knight_moves[abs(a-c)][abs(b-d)]

