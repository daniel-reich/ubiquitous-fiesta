
def find_coordinates(regions,coord):
    for i in regions:
        if coord in i:
            return True
    return False
​
def recursive_inspect(grid,coord,region):
​
    if grid[coord[0]][coord[1]] == 1 and coord not in region:
        region.add(coord)
    else:
        return region
​
    if coord[0] > 0 :
        recursive_inspect(grid,(coord[0]-1,coord[1]),region)
    if coord[1] < len(grid[coord[0]])-1:
        recursive_inspect(grid,(coord[0],coord[1]+1),region)
    if coord[0] < len(grid)-1:
        recursive_inspect(grid,(coord[0]+1,coord[1]),region)
    if coord[1] > 0 : 
        recursive_inspect(grid,(coord[0],coord[1]-1),region)
    return region
​
​
def num_regions(grid):
    i=0
    regions=[]
    region=set()
    
​
    while i < len(grid):
        j=0
        while j < len(grid[i]):
            if grid[i][j] == 1 and find_coordinates(regions,(i,j)) == False:
                regions.append(list(recursive_inspect(grid,(i,j),region)))
                region.clear()
            j+=1
        i+=1
​
    return len(regions)

