
def is_goal_scored(goal):
    for row in goal[:3]:
        if '0' in row[0] and 2 < row[0].index('0') < 8:
            return True
    return False

