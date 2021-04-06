
def record_temps(r, c):
    return [[min(i[0],j[0]),max(i[1],j[1])] for i,j in zip(r,c)]

