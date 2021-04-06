
def left_slide(tiles):
    '''
    Returns tiles after they have been merged to the left as per the rules of
    2048 described in the instructions.
    '''
    active_tiles = [tile for tile in tiles if tile]  # remove spaces
    merged_tiles = []
    
    i = 0
    size = len(active_tiles)
    while i < size:
        if i == size - 1:
            merged_tiles.append(active_tiles[i])  # last tile unchanged
            break
        if active_tiles[i] == active_tiles[i+1]:
            merged_tiles.append(active_tiles[i] * 2)  # merge the tiles
            i+= 2  # skip over next tile
        else:
            merged_tiles.append(active_tiles[i])
            i+= 1
        
    return merged_tiles + [0] * (len(tiles) - len(merged_tiles)) # 0 fill at right

