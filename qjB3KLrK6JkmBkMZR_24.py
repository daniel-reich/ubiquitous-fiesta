
def can_capture(queens):
    q1r = ord(queens[0][0])
    q2r = ord(queens[1][0])
    q1f = int(queens[0][1])
    q2f = int(queens[1][1])    
    return ((q1r==q2r)or (q1f==q2f) or (abs(q1r-q2r) == abs(q1f-q2f)) )

