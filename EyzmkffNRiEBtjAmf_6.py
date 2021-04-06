
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a, b, c, w, h):
    hole_area = w + h
    brick_face = a + b
    brick_long = a + c
    if brick_face == hole_area or brick_long == hole_area:
        return True
    else:
        return False

