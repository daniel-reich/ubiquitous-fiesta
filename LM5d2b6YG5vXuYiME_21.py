
def can_enter_cave(lst):
    rows = len(lst)
    cols = len(lst[0])
    
    start_col = 0
    end_col = cols - 1
    
    steps = [[1,0],[-1,0],[0,1],[0,-1]] 
    
    found = False
    for i in range(rows):
        stack = []
        if lst[i][start_col] == 0:
            stack.append([i,start_col])
        while len(stack) != 0:
            current = stack[-1]
            adj_available = False
            for step in steps:
                x = current[0] + step[0]
                y = current[1] + step[1]
                if (x >=0 and x <rows) and (y >=0 and y<cols):
                    if lst[x][y] == 0:
                        if y == end_col:
                            return True
                        lst[x][y] = 2
                        adj_available = True
                        
                        stack.append([x,y])
                        break
            if not adj_available:
                stack.pop()
                
    return False

