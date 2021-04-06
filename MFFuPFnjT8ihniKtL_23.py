
def bug_jump(height, time):
    g = 2 * 9 / 3 ** 2
    v = g * height ** 0.5 
    time /= 1000
    c_pos = round(v * time - time ** 2,2)
    if c_pos % 1 == 0:
        c_pos = int(c_pos)
    if c_pos < 0:
        return [0,None]
    else:
        return [c_pos,'up'] if v - 2 * time > 0 else [c_pos,'down']

