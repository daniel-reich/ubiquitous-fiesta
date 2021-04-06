
def ones_infection(arr):
    rows = []
    cols = []
    
    
    for x in range(len(arr)): 
        for y in range(len(arr[x])): 
            if arr[x][y]:
                rows.append(x)
                cols.append(y)
    
    for x in rows:
        arr[x] = [1] * len(arr[x])
    
    for x in cols:
        for y in range(len(arr)):
            arr[y][x] = 1
        
    
    return arr

