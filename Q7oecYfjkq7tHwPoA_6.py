
def climb(stamina, obstacles):
    count = 0
    for x, y in zip(obstacles, obstacles[1:]):
        count += 1
        dist = x - y
        if dist > 0:
            f = 1
        else:
            f = 2
        a, b = divmod(abs(dist), 1)
        if b > 0:
            a += 1
        stamina = stamina - (f * a)
        if stamina < 0:
            return count - 1
    return count

