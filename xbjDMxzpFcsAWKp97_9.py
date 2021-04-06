
def can_see_stage(seats):
    for row in range(0, len(seats[0])):
        for i, column in enumerate(seats[:-1]):
            current = seats[i][row]
            nextv = seats[i + 1][row]
            if nextv <= current:
                return False
    return True

