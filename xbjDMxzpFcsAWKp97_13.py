
def can_see_stage(seats):
    for i in range( len(seats[1]) ):
        for j in range( len(seats) - 1 ):
            if seats[j+1][i] > seats[j][i]:
                continue
            else:
                return False
    return True

