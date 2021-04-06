
def spreadWater(field, waterCoordinates):
    import numpy
    
    print(field)
    for water in waterCoordinates:
        for i in range(water[1] - 1, water[1] + 2):
            if i is not -1 and i < len(field[0]): 
                if field[water[0]][i] is not "w": 
                    field[water[0]][i] = '#'
                if water[0] is not 0:
                    if field[water[0] - 1][i] is not "w":
                        field[water[0] - 1][i] = '#'
                if water[0] < len(field) - 1:
                    if field[water[0] + 1][i] is not "w":
                        field[water[0] + 1][i] = '#'
    print(numpy.array(field))
    allWet = True
    for row in field:
        for tile in row:
            if tile is 'c':
                allWet = False
                break
    return allWet    
​
​
def crop_hydrated(field):
    waterCoordinates = []
    for row in range(len(field)):
        for tile in range(len(field[0])):
            if field[row][tile] is 'w':
                waterCoordinates.append((int(row), int(tile)))
    return spreadWater(field, waterCoordinates)

