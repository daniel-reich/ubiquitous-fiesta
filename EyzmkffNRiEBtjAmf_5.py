
def does_brick_fit(a,b,c, w,h):
  lst = [a, b, c]
  lst.remove(max(lst))
  x, y = lst
  return sum([x, y]) <= sum([w, h])

