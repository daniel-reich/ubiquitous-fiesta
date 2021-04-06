
def bomb(data):
    '''
    Given the coordintes of 3 points plus the time taken for a bomb blast to
    reach them, return a tuple giving the bomb's location as described above.
    '''
    # Trilateration formula courtesy of https://math.stackexchange.com/
    # questions/884807/find-x-location-using-3-known-x-y-location-using-
    # trilateration
    
    SOUND_SPEED = 0.343
​
    p1, p2, p3 = data
    x1, y1, r1 = p1[0], p1[1], p1[2] * SOUND_SPEED
    x2, y2, r2 = p2[0], p2[1], p2[2] * SOUND_SPEED
    x3, y3, r3 = p3[0], p3[1], p3[2] * SOUND_SPEED  # coordinates & distance
​
    if r1 == r2 == r3 == 0.0:
        return (x1, y1)   # they are all on top of the bomb!
​
    A = -2*x1 + 2*x2
    B = -2*y1 + 2*y2
    C = r1*r1 - r2*r2 - x1*x1 + x2*x2 - y1*y1 + y2*y2
    D = -2*x2 + 2*x3
    E = -2*y2 + 2*y3
    F = r2*r2 - r3*r3 - x2*x2 + x3*x3 - y2*y2 + y3*y3
​
    return (round((C*E - F*B) / (E*A - B*D)), round((C*D - A*F) / (B*D - A*E)))

