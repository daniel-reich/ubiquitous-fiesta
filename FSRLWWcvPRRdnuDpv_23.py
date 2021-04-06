
def time_to_eat(time: str) -> list:
    meals = (7, 12, 19)
    temp = [int(i) for i in time.split()[0].split(':')]
    if 'p.m.' in time:
        temp[0] += 12
​
    if temp[0] < meals[0]:
        if temp[1] == 0:
            return [meals[0] - temp[0], temp[1]]
        else:
            return [meals[0] - temp[0] - 1, 60 - temp[1]]
    elif temp[0] < meals[1]:
        if temp[1] == 0:
            return [meals[1] - temp[0], temp[1]]
        else:
            return [meals[1] - temp[0] - 1, 60 - temp[1]]
    elif temp[0] < meals[2]:
        if temp[1] == 0:
            return [meals[2] - temp[0], temp[1]]
        else:
            return [meals[2] - temp[0] - 1, 60 - temp[1]]
    else:
        if temp[1] == 0:
            return [meals[0] + 24 - temp[0], temp[1]]
        else:
            return [meals[0] + 24 - temp[0] - 1, 60 - temp[1]]

