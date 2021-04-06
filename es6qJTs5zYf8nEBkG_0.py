
def is_rectangle(coordinates):
    coordinates = set([eval(coord) for coord in coordinates])
    if len(coordinates) != 4: return False
    xcoords, ycoords = zip(*coordinates)
    return len(set(xcoords))==len(set(ycoords))==2

