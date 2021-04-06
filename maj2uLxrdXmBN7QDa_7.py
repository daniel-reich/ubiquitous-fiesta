
def bishop(start, end, n):
    if start == end:
        return True
    s_c, s_r = ord(start[0]) - 96, int(start[1])
    e_c, e_r = ord(end[0]) - 96, int(end[1])
    s_color, e_color = 0, 0
    if s_r % 2:
        if s_c % 2:
            s_color = 1
    else:
        if not s_c % 2:
            s_color = 1
    if e_r % 2:
        if e_c % 2:
            e_color = 1
    else:
        if not e_c % 2:
            e_color = 1
    if s_color == e_color:
        if n == 0:
            return False
        elif n == 1:
            if abs(s_r - e_r) == abs(s_c - e_c):
                return True
        else:
            return True
    return False

