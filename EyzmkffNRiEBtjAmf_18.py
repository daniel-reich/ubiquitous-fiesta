
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
    
    return (a*b== w*h) or (b*c== w*h) or (a*c== w*h)

