
def climb(stamina, obstacles):
    import math
    c = 0
    stamina_needed = 0
    for i in range(len(obstacles) - 1):
        r = math.ceil(abs(obstacles[i] - obstacles[i + 1]))
        if obstacles[i] <= obstacles[i + 1]:
            stamina_needed = r * 2
        if obstacles[i] > obstacles[i + 1]:
            stamina_needed = r
        if stamina - stamina_needed < 0:
            break
        stamina -= stamina_needed
        c += 1
    return c

