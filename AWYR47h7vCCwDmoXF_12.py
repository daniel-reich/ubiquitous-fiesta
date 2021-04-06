
def is_goal_scored(goal):
    lst1 = ["".join(goal[i])[3:8] for i in range(3)]
    return bool([True for i in lst1 if '0' in i])

