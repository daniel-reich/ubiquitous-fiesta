
def search_coefficients(height_max, time):
    a = -0.000001
    b = 0
    while a > -100:
        while b < 100:
            time_max = - b / (2 * a)
            if time_max > 0:
                height = a * time_max * time_max + b * time_max
                if height < height_max + 0.0001 and height >= height_max - 0.0001:
                    return a, b, time_max
            b += 0.00000001
        a -= 0.00000001
​
​
def bug_jump(height_max, time):
    where_fly = None
    a, b, time_max = search_coefficients(height_max, time)
    if time < 2 * time_max:
        if time > time_max:
            where_fly = 'down'
        else:
            where_fly = 'up'
    else:
        time = 0
    height = a * time * time + b * time
    height = round(height, 2)
    return [height, where_fly]

