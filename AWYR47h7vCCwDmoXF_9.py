
def is_goal_scored(arrays):
    goal_definition, ball_location, counter = [], [], 0
    for array in arrays:
        for i in range(0,len(list(array[0])),1):
            if list(array[0])[i] == "#" and len(goal_definition) < 2:
                goal_definition.append(i)
            if list(array[0])[i] == "0":
                ball_location.append(counter)
                ball_location.append(i)
        counter +=1
    return True if ball_location[1] > goal_definition[0] and ball_location[1] < goal_definition[1] and ball_location[0] <= 2 else False

