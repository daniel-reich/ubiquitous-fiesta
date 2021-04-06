
def crop_hydrated(field):
    '''
    Returns True if any crops in field are neighbours of a water source, as
    explained in the instructions, otherwise False
    '''
    height, width = len(field), len(field[0])
    neighbours = lambda r,c: [field[i][j] for i in range(max(0,r-1),min(r+2, height))\
                              for j in range(max(0,c-1),min(c+2,width)) \
                              if not (i==r and j==c)]
​
    return all(['w' in neighbours(i,j) for i in range(height) \
                for j in range(width) if field[i][j] == 'c'])

