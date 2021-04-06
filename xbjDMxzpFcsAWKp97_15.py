
def can_see_stage(seats):
    for j in range(0,len(seats)-1):
        for i in range(0,len(seats[0])):
            if seats[j][i] >= seats[j+1][i]:
                return False
​
    return True

