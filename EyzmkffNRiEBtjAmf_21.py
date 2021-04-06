
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
​
def does_brick_fit(a,b,c, w,h):
  return any(x=={w, h} for x in [{a,b}, {b, c}, {a, c}])

