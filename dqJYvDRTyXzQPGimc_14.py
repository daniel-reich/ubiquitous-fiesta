
def is_unfair_hurdle(h):
  if len(h) > 3:
    return(True)
​
  total_length = len(h[0])
  x = total_length - h[0].count("#")
  y = (x//(h[0].count("#") - 1))
​
  if y < 4:
    return(True)
  return(False)

