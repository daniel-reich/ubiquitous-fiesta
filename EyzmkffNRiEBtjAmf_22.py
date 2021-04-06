
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
  smallest = [a,b,c]
  smallest.remove(max([a,b,c]))
  return sorted(smallest)[0] <= sorted([w, h])[0] and sorted(smallest)[1] <= sorted([w, h])[1]

