
def bishop(start, end, n):
    n_start = (ord(start[0]) - 96, int(start[1]))
    n_end = (ord(end[0]) - 96, int(end[1]))
    if n == 0:
        return True if start == end else False
    if n >= 2:
        return True if abs(n_start[0] - n_start[1]) % 2 == abs(n_end[0] - n_end[1]) % 2 else False
    if n == 1:
        return True if abs(n_start[0] - n_end[0]) == abs(n_start[1] - n_end[1]) else False

