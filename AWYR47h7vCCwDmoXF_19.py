
def is_goal_scored(goal):
    goal_post = goal[0:3]
    for x in goal_post:
        x = "".join(x)
        ind_a = x.index("#")
        ind_b = x.rfind("#")
        if "0" in x[ind_a+1:ind_b]:
            return True
    return False

