
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
    brick = sorted([a, b, c])
    hole = sorted([w, h])
    return brick[0] <= hole[0] and brick[1] <= hole[1]

