
shift_left = lambda x, y, i=1: x if i == 2**y else x + shift_left(x, y, i+1)

